import discord
from discord.ext import commands
import os
import json


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    bot.unload_extension(F'cmds.test')
    print(">> Bot is online <<")

#----------------------------------------------------------------------------
bot.remove_command('help')
#help指令
@bot.group()
async def help(ctx):
    await ctx.send('普通功能：\n```css\n'
    +str(jdata['command_prefix'])+'ping 顯示機器人的延遲\n'
    +str(jdata['command_prefix'])+'ccc [基礎近戰暴率,連擊數,額外暴率加成] 計算近戰塞急進猛突暴率\n'
    +str(jdata['command_prefix'])+'wws [基礎近戰觸發,連擊數,額外觸發加成] 計算近戰塞創口潰爛觸發\n'
    +str(jdata['command_prefix'])+'sayd [msg] 使機器人說話\n'
    +str(jdata['command_prefix'])+'picture 隨機發送一張圖片\n'
    +str(jdata['command_prefix'])+'user 顯示個人訊息\n```僅限管理員的功能：\n```css\n'
    +str(jdata['command_prefix'])+'clear [num] 刪除指定數量的聊天內容\n```')

#leave
@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'看來 \n <@{member.id}> \n 離開唷 感謝你的陪伴')
#-----------------------------------------------------------------------------

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'已加載 {extension}')
    print(F'\n---------------------------------\n已加載 {extension}\n---------------------------------\n')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'已卸載 {extension}')
    print(F'\n---------------------------------\n已卸載 {extension}\n---------------------------------\n')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'已重新加載 {extension}')
    print(F'\n---------------------------------\n已重新加載 {extension}\n---------------------------------\n')
#機器人關閉系統--------------------------------------------   
@bot.command()
async def disconnect(ctx):
    print('機器人已關閉')
    await ctx.send('機器人已關閉') #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    await bot.close()
    
#--------------------------------

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')
    
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
