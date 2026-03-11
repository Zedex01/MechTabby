import requests #Use to talk to ai endpoint

def main(argc = None, argv = None):
	while True:
		msg = input("You: ")
		
		r = requests.post("http://localhost:11434/api/generate",
			json = {
				"model":"mistral:latest",
				"prompt": msg,
				"stream": False
			})

		try:
			reply = r.json()["response"].strip()
		except:
			reply = r.json()["error"].strip()

		print(reply)







if __name__ == "__main__":
	main()