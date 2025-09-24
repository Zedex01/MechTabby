""" Locate """
import discord, logging, re
from discord.ext import commands
from util.Linker import Linker
from util.Server import Server

logger = logging.getLogger(__name__)

class LocateStructure(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.lnkr = Linker()
        self.srv = Server()
        
    @commands.command(name="locate_structure", description="locates a stucture nearest the player who runs the command")
    async def locate_structure(self, ctx, structure) -> None:
        
        if structure == "list":
            embed = discord.Embed(
                title=f"Structures:",
                color=discord.Color.purple()
            )
            structures = [
                "ancient_city",
                "bastion_remnant",
                "buried_treasure",
                "desert_pyramid",
                "end_city",
                "fortress",
                "igloo",
                "jungle_pyramid",
                "mansion",
                "mineshaft",
                "mineshaft_mesa",
                "monument",
                "nether_fossil",
                "ocean_ruin_cold",
                "ocean_ruin_warm",
                "pillager_outpost",
                "ruined_portal",
                "ruined_portal_desert",
                "ruined_portal_jungle",
                "ruined_portal_mountain",
                "ruined_portal_nether",
                "ruined_portal_ocean",
                "ruined_portal_swamp",
                "shipwreck",
                "shipwreck_beached",
                "stronghold",
                "swamp_hut",
                "trail_ruins",
                "village_desert",
                "village_plains",
                "village_savanna",
                "village_snowy",
                "village_taiga"
            ]
            
            structure_list = "\n".join(structures)
            
            
            embed.add_field(name="List: ",value=structure_list, inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
            await ctx.send(embed=embed)
            return
        
        
        #Can be used on either self or another member of the discord
        player = ctx.author
        
        #Get the players ID from the json file
        playerName = self.lnkr.getMinecraftName(player.id)
        
        #Catch if it is not a linked account
        if playerName == None:
            await ctx.send(f"{player.display_name}'s account is not linked.")
            return
     
            
        #check if player is online:
        if not self.srv.playerOnline(playerName):
            await ctx.send(f"Currently {player.display_name} is not online.")
            return
            
        #Send a request for players coords to the server
        recv = self.srv.sendCmd(f"execute as {playerName} at @s run locate structure minecraft:{structure}")
        
        if recv == "":
            recv = "None could be found nearby..."
        
        else:
            recv = recv.replace("minecraft:","")
              
        
        embed = discord.Embed(
            title=f"📍 **{structure.capitalize()}**",
             color=discord.Color.purple()
        )
        embed.add_field(name="Search Results: ",value=recv, inline=True)

        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(LocateStructure(bot))
        
            