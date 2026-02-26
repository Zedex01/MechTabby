#
from flask import Flask, render_template, request

from pathlib import Path
import sys

import json

# === Consts ===
HOST = '127.0.0.1'
PORT = 5000

# === Paths ===
if getattr(sys, 'frozen', False):
	root_dir = Path(sys._MEIPASS).parent
else:
	root_dir = Path(__file__).parent

template_dir = root_dir / "templates"
src_dir = root_dir / "src"
data_dir = root_dir / "data"

# === Main ===
def main(argc = None, argv = None):
	print("Server Starting...")

	#Create Server Instance
	app = Flask(__name__)

	# === Pages ===
	@app.route('/')
	def root():
		return render_template('root.html')

	@app.route('/upload', methods=['GET', 'POST'])
	def upload():

		if request.method == 'POST':
			print("=========POST==================")

			for header in request.headers:
				print(header[0], ": ", header[1])

			#Convert data to json
			data = json.loads(request.get_data().decode())
			with open("output.json", "w") as f:
				json.dump(data, f, indent=4)

			print("Content Recived!")
			print("===============================")

		return "Request Recived!", 200 

	#Start Server Instace
	app.run(host=HOST,port=PORT)

	return 0

if __name__ == "__main__":
	main()
	
