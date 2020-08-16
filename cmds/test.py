import discord
from discord.ext import commands
from core.classes import Cog_Extension


class test(Cog_Extension):
    @commands.command()
    async def notice(self,ctx):
        await ctx.send(f'測試功能區域')

def setup(bot):
    bot.add_cog(test(bot))