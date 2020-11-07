import discord
from discord.ext import commands
import os
import json

os.system('pip install --upgrade pip')
os.system('pip install --upgrade discord.py')

intents = discord.Intents.all()


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='-',intents = intents)

@bot.event
async def on_ready():
    bot.unload_extension(F'cmds.test')
    print(">> Bot is online <<")

#----------------------------------------------------------------------------
bot.remove_command('help')
#help指令
@bot.group(name='help', aliases=['說明' , '機器人使用說明'])
async def help(ctx):
    await ctx.send('普通功能：\n```css\n'
    +str(jdata['command_prefix'])+'ping 顯示機器人的延遲\n'
    +str(jdata['command_prefix'])+'ccc [基礎近戰暴率 連擊數 額外暴率加成] 計算近戰塞急進猛突暴率\n'
    +str(jdata['command_prefix'])+'wws [基礎近戰觸發 連擊數 額外觸發加成] 計算近戰塞創口潰爛觸發\n'
    +str(jdata['command_prefix'])+'sayd [msg] 使機器人說話\n'
    +str(jdata['command_prefix'])+'picture 隨機發送一張圖片\n'
    +str(jdata['command_prefix'])+'calc [數學算式]簡易的運算(支援: + - * / ( ) 小數 科學記號)中間不能有空格 不支援指數運算 \n'
    +str(jdata['command_prefix'])+'user 顯示個人訊息\n```僅限管理員的功能：\n```css\n'
    +str(jdata['command_prefix'])+'clear [num] 刪除指定數量的聊天內容\n```')
    await ctx.send('這些指令的別名：\n```css\n'
    +str(jdata['command_prefix'])+'ping：[延遲 , 機器人延遲 , delay]\n'
    +str(jdata['command_prefix'])+'ccc：[急進猛突 , 急進 , 極盡]\n'
    +str(jdata['command_prefix'])+'wws：[創口潰爛 , 創口]\n'
    +str(jdata['command_prefix'])+'sayd：[說 , 機器人說]\n'
    +str(jdata['command_prefix'])+'picture：[pic , 圖片]\n'
    +str(jdata['command_prefix'])+'calc：[計算機 , 計算]\n'
    +str(jdata['command_prefix'])+'user：[使用者資訊 , 用戶資訊]\n'
    +str(jdata['command_prefix'])+'clear：[clean , 清除]\n```')

#@bot.command(name='alias', aliases=['別名'])
#async def alias(ctx):

 
#-----------------------------------------------------------------------------

@bot.command(name= 'load', aliases=['載入' , '載入模組'])
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'已加載 {extension}')
    print(F'\n---------------------------------\n已加載 {extension}\n---------------------------------\n')

@bot.command(name= 'unload', aliases=['卸載' , '卸載模組'])
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'已卸載 {extension}')
    print(F'\n---------------------------------\n已卸載 {extension}\n---------------------------------\n')

@bot.command(name= 'reload', aliases=['重載' , '重載模組' , '重新載入模組'])
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'已重新加載 {extension}')
    print(F'\n---------------------------------\n已重新加載 {extension}\n---------------------------------\n')
#機器人關閉系統--------------------------------------------   
@bot.command(name= 'disable', aliases=['disconnect' , 'shutdown' , '關閉機器人'])
async def disable(ctx):
    print('機器人已關閉')
    await ctx.send('機器人已關閉') #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    await bot.close()
    
#--------------------------------

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
        
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
