import asyncio
import websockets
import json


#Don't block main websocket comm while waiting for input from op
async def SendCommand(ws):
	loop = asyncio.get_event_loop()

	path = "PS"

	while True:
		ctx = await loop.run_in_executor(None, input, f"{path}> ")

		out = {"ctx": ctx}
		await ws.send(json.dumps(out))

		data = await ws.recv()
		data = json.loads(data)
		
		path = data["path"]

		raw_output = data["output"]

		#Print back to operator
		print("")
		for line in raw_output:
			print(line.rstrip())

		print("=====================================")



async def handler(ws):
	print("Client Connected!")
	try:
		#Print Device that connected
		device = await ws.recv()
		print(device)

		await SendCommand(ws)


	except websockets.ConnectionClosed:
		print("Client Disconnected")

async def main():
	async with websockets.serve(handler, "localhost", 8765):
		print("Server running")
		await asyncio.Future()


asyncio.run(main())