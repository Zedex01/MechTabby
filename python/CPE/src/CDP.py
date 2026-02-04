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
			"url":"https://lmi3d.com/account/?destination=https://www.google.com/"
		}
	}

	#Send it:
	ws.send(json.dumps(cmd))

	#Read Response:
	resp = ws.recv()
	#print(resp)

	#Get Page Tree Frame:
	cmd = {
		"id" : 2, #Unique for each command
		"method": "Page.getFrameTree",
		"params": {
			"url":"https://lmi3d.com/account/?destination=https://www.google.com/"
		}
	}

	#Send it:
	ws.send(json.dumps(cmd))

	#Read Response:
	resp = ws.recv()

	print("DOM.ENABLE:")

	#Enable DOM domain?
	cmd = {"id" : 3, "method": "DOM.enable"}
	ws.send(json.dumps(cmd))
	resp = ws.recv()

	# Get document root of a frame
	cmd = {"id": 4, "method": "DOM.getDocument", "params": {"depth": -1, "pierce": True}}
	ws.send(json.dumps(cmd))
	response = ws.recv()
	doc = json.loads(response)

	#Next
	cmd = {
    "id": 5,
    "method": "DOM.querySelectorAll",
    "params": {
        "nodeId": doc["result"]["root"]["nodeId"],
        "selector": "input, textarea"
        }
    }

	ws.send(json.dumps(cmd))

	while True:
		msg = json.loads(ws.recv())

		#Ignore Events:
		if "method" in msg:
			continue

		if msg.get("id") == 5:
			node_ids = msg["result"]["nodeIds"]
			break

	print(node_ids)
	exit()

	resp = ws.recv()
	print(resp)

	inputs = json.loads(resp)["result"]["nodeIds"]

	print(inputs)

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