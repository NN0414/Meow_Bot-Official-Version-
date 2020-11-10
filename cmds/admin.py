import discord
from discord.ext import commands
from core.classes import Cog_Extension


class admin(Cog_Extension):
    #清除訊息
    @commands.command(name='clear', aliases=['clean' , '清除'])
    async def clear(self,ctx,num:int):
        if ctx.message.author.id == ctx.guild.owner_id:
            await ctx.channel.purge(limit=num+1)
            print(str(ctx.message.author)+' ---ID '+str(ctx.message.author.id)+'在 << '+str(ctx.channel.name)+' >> 頻道使用了clear指令刪除了'+str(int(num))+'個對話')
            if num>=10:
              await ctx.send('https://tenor.com/view/explode-blast-blow-nuclear-boom-gif-15025770')
        else:
            await ctx.send('權限不足 本指令只提供給伺服器傭有者 \n本伺服器擁有者為 <@' + str(ctx.guild.owner_id) + '>')


def setup(bot):
    bot.add_cog(admin(bot))