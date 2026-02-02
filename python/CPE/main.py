'''
CPE
'''

import sqlite3, os, getpass, binascii
from pathlib import Path

#default_path = r'C:\Users\mmoran\AppData\Local\Google\Chrome\User Data\Default'

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


	with sqlite3.connect(db) as conn:
		cur = conn.cursor()
		cur.execute("SELECT origin_url, username_value, password_value FROM logins")
		res = cur.fetchall()

	for login in res:
		url, username, enc_password = login
		enc_password.strip()
		print(enc_password)

		try:
			dec_pass = binascii.hexlify(binascii.unhexlify(enc_password))

			print(f"URL: {url}\nUSERNAME: {username}, \nPASSWORD: {dec_pass.decode('utf-8')}\n")
		except:
			print("Skipped.")

if __name__ == "__main__":
	extract()