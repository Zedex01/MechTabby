from pathlib import Path

"""

Read From File For Payload


"""

with open('payload', 'r') as f:
	for line in f.readlines():
		#Split line into seperate parts
		tokens = line.split()

		if tokens[0] == "WRITE":
			print("Writing: ", tokens[1:])
		elif tokens[0] = "WAIT":
			print(f"Waiting {tokens[1]}s")
		elif tokens[0] = ""


