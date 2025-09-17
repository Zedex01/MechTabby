"""
For Communicating with the server via TCP connection

**NOTE: for this feature to work properly, 
you must configure your server.properties file correctly.

"""

from mcrcon import MCRcon
import os

class Server:
    def __init__(self) -> None:
        self.PORT = os.getenv('SERVER_PORT')
        self.PASS = os.getenv('SERVER_PASSWORD')
        
    def sendCmd(self, content: str) -> str:
        with MCRcon("127.0.0.1", self.PASS, port=int(self.PORT)) as mcr:
            output = mcr.command(content)
        return output
            
#TODO
    def isRunning(self) -> bool:
        with MCRcon("127.0.0.1", self.PASS, port=int(self.PORT)) as mcr:
            output = mcr.command('list')
        return output
    