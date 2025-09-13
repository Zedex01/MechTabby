import discord
from discord.ext import commands

#Copied from the discord api:
class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
