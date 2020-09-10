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
    #查詢user資訊
    @commands.command()
    async def user(self,ctx):
        arg = ctx.message.channel
        args = str(arg).split(' ')
        CMD = 'Direct Message with'
        CMDs = CMD.split(' ')
        msg = 'Author:'+str(ctx.message.author)+'\nAuthor ID:'+ str(ctx.message.author.id)+'\nChannel:'+str(ctx.message.channel)+'\nChannel ID:'+str(ctx.message.channel.id)
        if CMDs[0] == args[0] and CMDs[1] == args[1] and CMDs[2] == args[2]:
            print('私人訊息')
            await ctx.send(msg)
        else:
            print('群組訊息')
            msg = msg +'\nGuild.owner:'+str(ctx.guild.owner) +'\nGuild.owner_id:' +str(ctx.guild.owner_id)+'\nGuild.name:' +str(ctx.guild.name)
            await ctx.send(msg)
    #說
    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    #近戰有塞急進猛突暴擊機率計算器
    @commands.command()
    async def ccc(self,ctx,num:str):
      i1, i2, i3 = num.split(',')
      sum= float(i1) * ( 100 + 60 * ( float(i2) - 1 ) + float(i3) )  / 100
      #總暴率=基礎暴率× (1 + 急進猛突的加成 × (連擊倍率-1)+其他暴擊加成)
      await ctx.send(f'近戰總爆擊機率：' + str(sum) + '%')
    #創口觸發版 類似同上
    @commands.command()
    async def wws(self,ctx,num:str):
      i1, i2, i3 = num.split(',')
      sum= float(i1) * ( 100 + 40 * ( float(i2) - 1 ) + float(i3) )  / 100
      #總觸發=基礎觸發× (1 + 觸發加成 × (連擊倍率-1)+其他暴擊加成)
      await ctx.send(f'近戰總觸發機率：' + str(sum) + '%')
    @commands.command()
    async def sendch(self,ctx,chid,*,msg):
        ch = self.bot.get_channel(int(chid))
        await ch.send(msg)

    @commands.command()
    async def send(self,ctx,userid,*,msg):
        if '!' in userid:
            user = str(userid).split('!')
        else:
            user = str(userid).split('@')
        if str.isdigit(user[0]):
            user2 = self.bot.get_user(int(userid))
            await user2.send(msg)
        else:
            user1 = str(user[1]).split('>')
            user2 = self.bot.get_user(int(user1[0]))
            await user2.send(msg)

def setup(bot):
    bot.add_cog(Common(bot))