### GENERAL OUTLINE ###

Simple loop:

CS runs on targeted dns, waits for a connection, once recieved opens a comms channel
Terminal for inputing commands


Tr runs on client machine, Continously tries to reach out to server. Once connected hands over control with access to terminal command line.

On Connection:
	Provides IP, MAC, Hostname/devicename, User


### The Process ###

"""Prevents the need to configure targets router"""

SERVER SIDE:
	Setup WS server
	Setup SSH Server

CLIENT SIDE:
Run installer (as Admin):
	- Puts the RAT in the correct spot
	- Sets it up to autorun using Regkey "Run"

From CommandServer:

Once Connected:
	Setup and run reverse ssh back to the server from target

Open ssh connection and go to town

Can use autossh to always try to connect back to ther server


### Setting up ssh server ###
