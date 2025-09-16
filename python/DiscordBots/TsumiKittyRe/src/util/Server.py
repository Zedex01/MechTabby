"""
For Communicating with the server via TCP connection

**NOTE: for this feature to work properly, 
you must configure your server.properties file correctly.

"""

from mcrcon import MCRcon
import os

class Server():
    def __init__(self):
        self.PORT = os.getenv('SERVER_PORT')
        self.PASS = os.getenv('SERVER_PASSWORD')
        
    def sendCmd(content):
        with MCRcon("127.0.0.1", self.PASS, port=int(self.PORT)) as mcr:
            output = mcr.command(content)
        
        return output
    