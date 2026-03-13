import asyncio
import websockets

async def handler(websocket):
	print("Client Connected")

	try: 
		async for msg in websocket:
			print("Recived: ", msg)


			reply = f"Server got: {msg}"
			await websocket.send(reply)

	except websockets.ConnectionClosed:
		print("Client Disconnected")

async def main():
	async with websockets.serve(handler, "localhost", 8765):
		print("Server Running on ws://localhost:8765")
		await asyncio.Future() #Run Forever


asyncio.run(main())