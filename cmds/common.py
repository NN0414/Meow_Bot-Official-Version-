import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Common(Cog_Extension):
    #ping
    @commands.command(name= 'ping', aliases=['延遲' , '機器人延遲' , 'delay'])
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} 毫秒 (ms)')  
    #隨機傳送圖片網址
    @commands.command(name= 'picture', aliases=['pic' , '圖片'])
    async def picture(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)
    #查詢user資訊
    @commands.command(name= 'user', aliases=['使用者資訊' , '用戶資訊'])
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
    @commands.command(name= 'sayd', aliases=['說' , '機器人說'])
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
        
    #近戰有塞急進猛突12x下的暴擊機率計算器
    @commands.command(name='ccc', aliases=['急進猛突' , '急進' , '極盡'])
    async def ccc(self,ctx, *args):
      msg = self.BloodRush(' '.join(args))
      await ctx.send(msg)

    def BloodRush(self,num):
      i1, i2, i3 = num.split(' ')
      if int(i2) <= 13:
        sum= float(i1) * ( 100 + 60 * ( float(i2) - 1 ) + float(i3) )  / 100
        #總暴率=基礎暴率× (1 + 急進猛突的加成 × (連擊倍率-1)+其他暴擊加成)
        return ('近戰總爆擊機率：' + str(sum) + '%')
      else:
        return ('連擊最高只有到 13x 啦')
    #----------------------------------
    #近戰有塞創口潰爛12x下的觸發機率計算器    
    @commands.command(name= 'wws', aliases=['創口潰爛' , '創口'])
    async def wws(self,ctx,*args):
      msg = self.WeepingWounds(' '.join(args))
      await ctx.send(msg)

    def WeepingWounds(self,num):
      i1, i2, i3 = num.split(' ')
      if int(i2) <= 13:
        sum= float(i1) * ( 100 + 40 * ( float(i2) - 1 ) + float(i3) )  / 100
        #總觸發=基礎觸發× (1 + 觸發加成 × (連擊倍率-1)+其他觸發加成)
        return ('近戰總觸發機率：' + str(sum) + '%')
      else:
        return ('連擊最高只有到13x啦')

    @commands.command(name= 'sendch', aliases=['發送至頻道'])
    async def sendch(self,ctx,chid,*,msg):
        ch = self.bot.get_channel(int(chid))
        await ch.send(msg)
    
    @commands.command(name= 'send', aliases=['私訊'])
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
    @commands.command()
    async def 環形裝置(self,ctx):
      await ctx.send(f'```維加環形裝置→太空站          & 微蟎蛛型機\n告達環形裝置→昇華實驗室      & 賽托蛛型機(瓦內蜘蛛)\n索拉環形裝置→潤盈寺          & 凱塔蛛型機\n聖油環形裝置→利潤收割者圓蛛\n天藍環形裝置→剝削者圓蛛```')
    
    @commands.command(name= 'Milos', aliases=['香蕉君' , '象徵自由的男人'])
    async def Milos(self,ctx):
      #await ctx.channel.purge(limit=1)
      await ctx.send(self.bot.get_emoji(int(710157217948631085)))
    
def setup(bot):
    bot.add_cog(Common(bot))