"""
Chrome DevTools Protocals

"""

import requests
import websocket
import json

def main():
	print("Starting...")

	#Get the websocket debugger url
	try:
		resp = requests.get("http://localhost:9222/json")

	except:
		print("Could Not Connect")
		return
	tabs = resp.json()

	#pull url from the first tab
	ws_url = tabs[0]["webSocketDebuggerUrl"]
	print(ws_url)

	#ws_url is where we send the commands

	ws = websocket.create_connection(ws_url)

	#Send example command to change page:
	cmd = {
		"id" : 1, #Unique for each command
		"method": "Page.navigate",
		"params": {
			"url":"https://lmi3d.com/"
		}
	}

	#Send it:
	ws.send(json.dumps(cmd))

	#Read Response:
	resp = ws.recv()
	print(resp)

	#close Connection:
	ws.close()



def PrintOpenTabs():

	#Minimal example, get open tabs:
	try:
		resp = requests.get("http://localhost:9222/json")
	
	except Exception as e:
		print(e)
		return

	tabs = resp.json()

	for tab in tabs:
		print(tab["id"], tab["title"], tab["url"])

if __name__ == "__main__":
	main()