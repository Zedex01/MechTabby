""" find """
import discord, logging, re
from discord.ext import commands
from src.util.Linker import Linker
from src.util.Server import Server

logger = logging.getLogger(__name__)

class Find(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.lnkr = Linker()
        self.srv = Server()
        
    @commands.command(name="find", description="finds players, structures, biomes (coming soon)")
    @commands.guild_only()

    async def Find(self, ctx, arg1: discord.Member = None, arg2 = None) -> None:

        #If there is no second argument
        if not arg2:
            #Can be used on either self or another arg1 of the discord
            

            #Check if argument is a valid discord member
            try:
                player = arg1 or ctx.author
                #Get the players ID from the json file
                playerName = self.lnkr.getMinecraftName(player.id)
            except Exception as e:
                await ctx.send("Not a valid argument, please use !help for uses")
                return


            #Catch if it is not a linked account
            if playerName == None:
                await ctx.send(f"{player.display_name}'s account is not linked.")
                return

            #check if player is online:
            if not self.srv.playerOnline(playerName):
                await ctx.send(f"Currently {player.display_name} is not online.")
                return

            #Send a request for players coords to the server
            recv = self.srv.sendCmd(f"data get entity {playerName} Pos")
            recv = re.findall(r"(-?\d+\.\d+)", recv)
            coords = []
            for value in recv:
                coords.append(f"{float(value):.1f}")       

            coords_formatted = ", ".join(coords)

            embed = discord.Embed(
                title=f"📍 **{playerName}**",
                 color=discord.Color.blue()
            )
            embed.add_field(name="Coordinates: ",value=coords_formatted, inline=True)

            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)

            await ctx.send(embed=embed)





async def setup(bot):
    await bot.add_cog(Find(bot))
        
            