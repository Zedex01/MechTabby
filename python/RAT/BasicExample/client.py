import asyncio
import websockets

async def run():
	url = "ws://localhost:8765"

	try:
		async with websockets.connect(url) as websocket:
			print("Connected to server")
	
	
			while True:
				msg = input("Send Message: ")
	
				await websocket.send(msg)
	
				reply = await websocket.recv()
				print("Server says:", reply)

	except:
		print("No Connection can be made...")

asyncio.run(run())