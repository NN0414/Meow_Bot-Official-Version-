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
    #隨機傳送圖片網址
    @commands.command()
    async def picture(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)
    #查詢user資訊
    @commands.command()
    async def user(self,ctx):
        await ctx.send('Author:'+str(ctx.message.author)+
        '\nAuthor ID：'     +str(ctx.message.author.id)+
        '\nChannel：'       +str(ctx.message.channel)+
        '\nChannel ID：'    +str(ctx.message.channel.id)+
        '\nGuild.owner：'   +str(ctx.guild.owner)+
        '\nGuild.owner_id：'+str(ctx.guild.owner_id)+
        '\nGuild.name：'    +str(ctx.guild.name))
    #說
    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    #近戰有塞急進猛突12x下的暴擊機率計算器
    @commands.command()
    async def ccc(self,ctx,num:str):
      i1, i2 = num.split(',')
      sum= float(i1) * ( 760 + float(i2) ) / 100
      await ctx.send(f'近戰總爆擊機率：' + str(sum) + '%')


def setup(bot):
    bot.add_cog(Common(bot))