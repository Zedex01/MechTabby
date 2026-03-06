## Ollama Setup ##

start ai endpoint for server:	
	ollama serve <model>

flags include:
                                                 
`--port <PORT>` | Change the listening port. Default is `11434`. 
Example: `ollama serve mistral --port 5000`        

`--host <HOST>` | Bind to a specific host/IP. Default is `localhost`. 
Example: `--host 0.0.0.0` to allow network access.

`--verbose`     | Show more logging in the terminal. Good for debugging or monitoring requests. 

`--quiet`       | Minimal logging.

`--log <FILE>`  | Write server logs to a file for monitoring.

