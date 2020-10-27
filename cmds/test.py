import discord
from discord.ext import commands
from core.classes import Cog_Extension

class test(Cog_Extension):
    #清除訊息
    @commands.command()
    async def t(self,ctx):
      await ctx.send("測試用地區")
  
def setup(bot):
    bot.add_cog(test(bot))