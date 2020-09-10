import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
      if '<@!737611092653637684>' in str(msg.content):
        await msg.add_reaction(self.bot.get_emoji(int(710157217948631085)))
      if '<@737611092653637684>' in str(msg.content):
        await msg.add_reaction(self.bot.get_emoji(int(710157217948631085)))
      if str(msg.channel.type) == 'private':
          print(str(msg.author) + '說:' + msg.content)
      else:
          if msg.guild.id == 552875885070516235:
              print(str(msg.author) + '說:' + msg.content)
      pass
  

def setup(bot):
    bot.add_cog(event(bot))