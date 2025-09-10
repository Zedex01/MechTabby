#Matthew Moran 2025-09-10

# py -c "import sys; print(sys.executable)"  
# To Install: py -m pip install -U discord.py

#Python Style guide:
#| Item                | Convention                      | Example                             |
#| ------------------- | ------------------------------- | ----------------------------------- |
#| Variable / Function | lowercase_with_underscores    | `total_score`, `send_message`       |
#| Class               | CapWords / PascalCase           | `UserProfile`, `DiscordBot`         |
#| Constant            | UPPERCASE_WITH_UNDERSCORES    | `MAX_CONNECTIONS`, `DEFAULT_PREFIX` |
#| Module / Package    | lowercase_with_underscores    | `my_module`, `utils`                |
#| Private (internal)  | _single_leading_underscore   | `_helper_method`                    |
#| Private (mangled)   | __double_leading_underscore | `__private_var`                     |

 #pyright: ignore[reportMissingImports]

import discord, os
from client.MyClient import MyClient

TOKEN = os.getenv('TSUMIKITTY_KEY')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
