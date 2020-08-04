import discord
from discord.ext import commands
from core.classes import Cog_Extension

class admin(Cog_Extension):
    #清除訊息
    @commands.command()
    async def clear(self,ctx,num:int):
        if ctx.message.author.id == 436866339731275787:
            await ctx.channel.purge(limit=num+1)
            print(str(ctx.message.author)+' ---ID '+str(ctx.message.author.id)+'在 << '+str(ctx.channel.name)+' >> 頻道使用了clear指令刪除了'+str(int(num))+'個對話')
        else:
            await ctx.send(f'您沒有權限使用此功能') 


def setup(bot):
    bot.add_cog(admin(bot))