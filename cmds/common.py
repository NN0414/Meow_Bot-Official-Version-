import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Common(Cog_Extension):
    #ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')  
    #隨機傳送圖片
    @commands.command()
    async def picture(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file= pic)
    #隨機傳送圖片網址
    @commands.command()
    async def web(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)
    #查詢user ID 和 Channel ID
    @commands.command()
    async def user(self,ctx):
        await ctx.send('Author:'+str(ctx.message.author)+'\nAuthor ID:'+ str(ctx.message.author.id)+
        '\nChannel:'+str(ctx.message.channel)+'\nChannel ID:'+str(ctx.message.channel.id))


def setup(bot):
    bot.add_cog(Common(bot))