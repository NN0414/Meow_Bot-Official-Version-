import discord
from discord.ext import commands
from core.classes import Cog_Extension
import os


class test(Cog_Extension):
    #清除訊息
    @commands.command(name='test', aliases=['機器人測試', '測試'])
    async def t(self,ctx):
      await ctx.send("test")
      print("test")
    @commands.command(name='memtest')
    async def memtest(self,ctx,uid):
      guild = self.bot.get_guild(552875885070516235)
      member = guild.get_member(int(uid))
      await ctx.send(member)
      print(member)

  
def setup(bot):
    bot.add_cog(test(bot))