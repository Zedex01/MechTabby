from flask import Flask, render_template, request
import sys


HOST = "127.0.0.1"
PORT = 5000


# === Main ===
def main(argc = None, argv = None):
	print("Server Starting...") 

	#Create Server Instance
	app = Flask(__name__)

	# === Pages ===
	@app.route('/')
	def root():
		return 0;

	@app.route('/upload', methods=['GET', 'POST'])
	def upload():

		if request.method == 'POST':
			print("=========POST==================")

			for header in request.headers:
			        print(header[0], ": ", header[1])

			time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
			file = time_stamp + ".json"
			file_path = data_dir / file

			#Convert data to json
			data = json.loads(request.get_data().decode())
			with open(file_path, "w") as f:
			        json.dump(data, f, indent=4)

			print("===============================")

		return "Request Recived!", 200 

	#Start Server Instace
	app.run(host=HOST,port=PORT)
	print("Waiting on connection...")
	return 0

if __name__ == "__main__":
	main()