import requests #Use to talk to ai endpoint

from pathlib import Path

#=======================
#	Constants
#=======================
HISTORY_SIZE = 100

conversation = []

"""
Prompt Archecture:

Scenario: You are texting the user as their friend {{name}}.

Personality: []

Rules: " Short messages, casual texting style, 1-2 sentances"

History: []

Looks: []

User Interests: [] ???


"""

sys_prompt = """
You are texting the user as their friend Nikki.

You are 22, and love racing japanese cars. love clubbing and rave music.

Rules:
- short messages
- casual texting style
- 1-2 sentences

Conversation History:
"""


def main(argc = None, argv = None):
	while True:
		msg = input("You: ")
		
		conversation.append(f"User: {msg}")

		prompt = sys_prompt + "\n".join(conversation) + "\nNikki:"

		r = requests.post("http://localhost:11434/api/generate",
			json = {
				"model":"mistral",
				"prompt": prompt,
				"stream": False
			})






if __name__ == "__main__":
	main()