import discord
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime,timedelta
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
      f = '[%Y-%m-%d %H:%M:%S]'
      time_delta = timedelta(hours=+8)
      utc_8_date_str = (datetime.utcnow()+time_delta).strftime(f)
      if '<@!737611092653637684>' in str(msg.content):
        await msg.add_reaction(self.bot.get_emoji(int(710157217948631085)))
      if '<@737611092653637684>' in str(msg.content):
        await msg.add_reaction(self.bot.get_emoji(int(710157217948631085)))
      if str(msg.channel.type) == 'private' and msg.author != self.bot.user:
        print(str(msg.author) + '私人或其他群組說:' + msg.content)
        fp = open("Private.log", 'a')
        fp.write(utc_8_date_str + str(msg.author) + '說：\n' + msg.content+'\n')
        fp.close()
      else:
        if str(msg.channel.type) == 'text' and msg.guild.id == 552875885070516235 and msg.author != self.bot.user:
            print(str(msg.author) + '在群組內說:' + msg.content)
            fp = open("Guild.log", 'a',encoding='utf8')
            fp.write(utc_8_date_str + str(msg.author) + '說：\n' + msg.content+'\n')
            fp.close()
      fp = open("All.log", 'a',encoding='utf8')
      fp.write(utc_8_date_str + str(msg.author) + '說：\n' + msg.content+'\n')
      fp.close()
      pass

def setup(bot):
    bot.add_cog(event(bot))