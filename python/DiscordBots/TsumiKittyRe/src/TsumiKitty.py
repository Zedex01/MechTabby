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

import discord, os, asyncio
from bot.Bot import Bot
from commands import *
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TSUMIKITTY_KEY')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = Bot(command_prefix="!", intents=intents)

#Setup Env

#Loading modular commands (cogs)
async def load_extensions():
    #await bot.load_extension("commands.GetIp")
    await bot.load_extension("commands.GetServerStatus")


# Main Function
async def main():
    async with bot:
        await load_extensions() #Load all command classes
        await bot.start(TOKEN)

# Launch
if __name__ == "__main__":
    asyncio.run(main()) #Start the main Function