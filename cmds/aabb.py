from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jset:
    jdata = json.load(jset)

stat = 0
aabbans = ''
aabblist = []
aabbPasswordAutoReset = 0
aabbPasswordStatus = 0
aabbPassword = []
def jud(num):
    a = int(num/1000)
    b = int((num/100)%10)
    c = int((num/10)%10)
    d = int(num%10)
    judlist = [a,b,c,d]
    if len(judlist) != len(set(judlist)):
        return False
    else:
        return True

def gamejud(num):
    global aabblist
    AA = 0
    BB = 0
    a = int(num/1000)
    b = int((num/100)%10)
    c = int((num/10)%10)
    d = int(num%10)
    judlist = [a,b,c,d]
    removelist = []
    for i in range(4):
        if judlist[i] == aabblist[i]:
            AA+=1
            removelist.append(judlist[i])
    set1 = set(removelist)
    set2 = set(judlist)
    set3 = list(set2 - set1)
    #print(set3)
    for i in set3:
        if i in aabblist:
            BB += 1
    return (str(AA)+'A'+str(BB)+'B')

def aabbPasswordGameReset():
    global aabbPasswordStatus,aabbPassword
    aabbPasswordStatus = 0
    aabbPassword = []
    if aabbPasswordAutoReset == 1:
        aabbPasswordStatus = 1  
        rannum = random.randint(1,100)
        aabbPassword.append([rannum,1,100])

class aabb(Cog_Extension):
    @commands.group()
    async def aabb(self,ctx):
        global stat
        if stat == 1:
            await ctx.message.delete()
            ans = str(ctx.message.content).split(',aabb ')
            if str.isdigit(ans[1]):
                if len(ans[1]) == 4 and isinstance(int(ans[1]),int):
                    if jud(int(ans[1])):
                        if gamejud(int(ans[1])) == '4A0B':
                            await ctx.send(str(ans[1]) +' - '+gamejud(int(ans[1])) + ' 遊戲結束\n'+'勝者<@'+str(ctx.author.id)+'>')
                            global aabbans,aabblist
                            stat = 0
                            aabbans = ''
                            aabblist = []
                            return stat,aabbans,aabblist
                        else:
                            await ctx.send(str(ans[1]) +" - "+ gamejud(int(ans[1])) +' - '+ctx.author.name)
                    else:
                        await ctx.send('請輸入4個數字 並且不重複')
                else:
                    await ctx.send('請輸入4個數字 並且不重複')
            else:
                pass
                #await ctx.send('賣來亂！')
        pass

    @aabb.command()
    async def start(self,ctx):
        global stat
        if stat == 1 :
            await ctx.send('遊戲已開啟！')
            return 0
        guild = self.bot.get_guild(ctx.message.guild.id)
        member = guild.get_member(ctx.author.id)
        roles = []
        for i in member.roles:
            roles.append(i.name)
        #if '⫍管理小仙君⫎' in roles or str(ctx.message.author.id) == jdata['owner'] or ctx.message.author.id == ctx.guild.owner_id:
        global aabbans,aabblist
        time = 0
        #aabblist = []
        a = random.randint(0,9)
        aabblist.append(a)
        while time < 3:
            time += 1
            a = random.randint(0,9)
            while a in aabblist:
                a = random.randint(0,9)
            aabblist.append(a)
        for i in aabblist:
            aabbans = aabbans + str(i)
        print(aabbans)
        stat = 1
        await ctx.send('AABB遊戲開始')
        user = self.bot.get_user(int(jdata['owner']))
        await user.send(str(aabbans))
        return aabbans,stat,aabblist

    @aabb.command()
    async def reset(self,ctx):
        guild = self.bot.get_guild(ctx.message.guild.id)
        member = guild.get_member(ctx.author.id)
        roles = []
        for i in member.roles:
            roles.append(i.name)
        if ctx.message.author.id == ctx.guild.owner_id:
            global stat,aabbans,aabblist
            if stat == 1:
                stat = 0
                tans = aabbans
                aabbans = ''
                aabblist = []
                await ctx.send('遊戲以重置\n上一局答案為'+tans)
            else:
                await ctx.send('遊戲尚未開始')
            return stat,aabbans,aabblist

    @aabb.command(name='help', aliases=['rule'])
    async def help(self,ctx):
        await ctx.send('```\n'
        +'AABB指令：\n'
        +'  '+str(jdata['command_prefix'])+'aabb start　開始遊戲\n'
        +'  '+str(jdata['command_prefix'])+'aabb reset　重置遊戲並顯示上局答案\n'
        +'  當遊戲開始後輸入 '+str(jdata['command_prefix'])+'aabb [數字] 即可遊玩\n'
        +'AABB規則：\n'
        +'  ,aabb 輸入4位數字 \n'
        +'  若答案中有此數字且位子正確即為A\n'
        +'  若答案中有此數字但位子錯誤即為B\n'
        +'ex：\n'
        +'  答案為　2360\n'
        +'  輸入　3260 = 2A2B\n'
        +'  輸入　4519 = 0A0B\n'
        +'  輸入　3461 = 1A1B\n'
        +'```')

    
    @commands.command(name='終極密碼autoreset', aliases=['autoreset'])
    async def 終極密碼autoreset(self,ctx,index:int=9999999):
        global aabbPasswordAutoReset
        if int(index) == 9999999:
            if aabbPasswordAutoReset == 0:
                aabbPasswordAutoReset = 1
                await ctx.send('終極密碼自動重啟已開啟')
            elif aabbPasswordAutoReset == 1:
                aabbPasswordAutoReset = 0
                await ctx.send('終極密碼自動重啟已關閉')
        elif int(index) == 0:
            aabbPasswordAutoReset = 0
            await ctx.send('終極密碼自動重啟已關閉')
        elif int(index) == 1:
            aabbPasswordAutoReset = 1
            await ctx.send('終極密碼自動重啟已開啟')
        if aabbPasswordAutoReset == 1:
            print('終極密碼自動重啟已開啟')
        else:
            print('終極密碼自動重啟已關閉')

    @aabb.command(name='終極密碼', aliases=['s'])
    async def 終極密碼(self,ctx):
        global aabbPasswordStatus,aabbPassword
        if aabbPasswordStatus == 0:
            aabbPasswordStatus = 1
            rannum = random.randint(1,100)
            print(rannum)
            aabbPassword.append([rannum,1,100])
            print(aabbPassword)
            await ctx.send('終極密碼！！\n遊戲開始 範圍1~100')
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if aabbPasswordStatus == 1 and msg.channel.id == 785021968415850516:
            if msg.content.isdigit():
                global aabbPassword
                if int(msg.content) == aabbPassword[0][0]:
                    await msg.channel.send('恭喜 '+str(msg.author)+' 猜對')
                    await msg.channel.send('https://tenor.com/view/explode-blast-blow-nuclear-boom-gif-15025770')
                    aabbPasswordGameReset()
                else:
                    if int(msg.content) <= aabbPassword[0][1] or int(msg.content) >= aabbPassword[0][2]:
                        await msg.channel.send(str(msg.author)+'你在跟我開玩笑嗎？')
                        return
                    elif int(msg.content) < aabbPassword[0][0] and int(msg.content) > aabbPassword[0][1]:
                        aabbPassword[0][1] = int(msg.content)
                        print('小數字已變更')
                    elif int(msg.content) > aabbPassword[0][0] and int(msg.content) < aabbPassword[0][2]:
                        aabbPassword[0][2] = int(msg.content)
                        print('大數字已變更')
                    await msg.channel.send(str(aabbPassword[0][1])+' ~ '+str(aabbPassword[0][2]))
                    print(aabbPassword)
                        
        pass

    '''@aabb.command()
    async def ans(self,ctx):
        if str(ctx.author.id) == jdata['owner']:
            if aabbans == '':
                await ctx.send('遊戲尚未開始')
                return
            await ctx.send(str(aabbans))'''


def setup(bot):
    bot.add_cog(aabb(bot))