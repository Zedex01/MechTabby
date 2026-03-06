import requests #Use to talk to ai endpoint

def main(argc = None, argv = None):
	while True:
		msg = input("You: ")
		
		r = requests.post("http://localhost:11434/api/generate",
			json = {
				"model":"mistral",
				"prompt": msg
			})

		reply = r.json()
		#reply = r.json()["response"].strip()

		print(reply)







if __name__ == "__main__":
	main()