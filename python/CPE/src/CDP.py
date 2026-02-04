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
		print("Could Not Get Json.")
		return

	tabs = resp.json()

	#pull url from the first tab
	ws_url = tabs[0]["webSocketDebuggerUrl"]
	print(ws_url)

	#ws_url is where we send the commands

	ws = websocket.create_connection(ws_url)

	#Enable Autofill:
	cmd = {"id": 1,"method": "Autofill.enable","params": {}}
	ws.send(json.dumps(cmd))
	resp = getResp(ws, 1)

	#Allow pages to send notifications/popups:
	cmd = {"id": 2,"method": "Page.enable","params": {}}
	ws.send(json.dumps(cmd))
	resp = getResp(ws, 2)

	#Navigate to a new page
	cmd = {"id": 3, "method": "Page.navigate",
		"params": {"url":"https://id.manulife.ca/"}
	}
	ws.send(json.dumps(cmd))

	#Now we listen for a new popup...
	cnt = 0
	while True:
		cnt += 1
		resp = json.loads(ws.recv())

		if "method" in resp and not "id" in resp:
				print("== Got event! ==")
				
				print("method: ", resp["method"])
				print("params: ", resp["params"])

		if cnt > 100:
			break
	exit()

	#Try Autofill
	cmd = {
	"id": 6,
	"method":"Autofill.trigger",
	"params": {
		"fieldId": user_id["result"]["nodeId"]
		}
	}

	ws.send(json.dumps(cmd))

	while True:
		resp = json.loads(ws.recv())
		if resp.get("id") == 6:
			break

	print(resp)


	#close Connection:
	ws.close()



def runCommands():
	for id in range(len(commands) - 1):
		runCommand(id + 1, commands[id])

def runCommand(id, value):
	method, params = value
	cmd = {"id": id, "method": method, "params": params}
	ws.send(json.dumps(cmd))

def getResp(ws, id):
	while True:
		resp = json.loads(ws.recv())
		if resp.get("id") == id:
			break
	return resp


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