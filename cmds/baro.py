from discord.ext import commands
from core.classes import Cog_Extension
import requests
import json
import asyncio
from datetime import datetime


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

rawDict = requests.get("https://raw.githubusercontent.com/lonnstyle/riven-mirror/dev/src/i18n/lang/zh-Hant.json")
Dict = json.loads(rawDict.text)
Dict = Dict['messages']


class baro(Cog_Extension):
  @commands.command(name='baroAuto')
  async def baro(self,ctx):
    came = False
    await ctx.send("Ordis正在監視Baro Ki'Teer")
    while came == False:
      url = requests.get("https://api.warframestat.us/pc/tc/voidTrader")
      html = json.loads(url.text)
      if html['active'] == True:
        message = "```"
        for items in html['inventory']:
          item = items['item']
          item = item.lower()
          item = item.replace("\'","")
          count = 0
          name = ''
          for words in item.split():
            if count != 0:
              word = words.capitalize()
              name += word
            elif count == 0:
              name += words
            count += 1
          name = Dict.get(name,name)
          ducats = items['ducats']
          credits = items['credits']
          message += f"物品:{name}\n杜卡德金幣:{ducats}\t現金:{credits}\n"
        message += "```"
        await ctx.send(message)
      timeLeft = html['activation']
      second = datetime.strptime(timeLeft,'%Y-%m-%dT%X.000Z')
      now = datetime.now()
      difference = second-now
      second = difference.days *24*60*60 +difference.seconds
      came = True
      await asyncio.sleep(second)
    if came == True:
      timeLeft = html['expiry']
      second = datetime.strptime(timeLeft,'%Y-%m-%dT%X.000Z')
      now = datetime.now()
      difference = second-now
      second = difference.days *24*60*60 +difference.seconds
      await asyncio.sleep(second)
      came = False


def setup(bot):
    bot.add_cog(baro(bot))
