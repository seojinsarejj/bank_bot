import asyncio, discord
from discord.ext import commands

from config import token,account
from service.crawling import Crawling


my_id = account['id']
pw = account['pw']
my_token = token
game = discord.Game("도움말 : !도움말")



bot = commands.Bot(command_prefix='!', status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
    print('봇 시작')


@bot.command()
async def 거래내역(ctx):
    await ctx.send("잠시만 기다려주세요")
    try:
        crawling = Crawling(my_id,pw)
        embed=discord.Embed(title="내 거래 내역", color=0x00ff56)
        result = crawling.get_transaction(3,50)
        for i in range(len(result)):
            embed.add_field(
                name=str(result[i][0]), 
                value= result[i][1] + " " + result[i][2]  + " " + str(result[i][3]) + " " + str(result[i][4]) + " " + str(result[i][5]) + " " + result[i][6],
                inline=False)

        await ctx.send(embed=embed)
    except:
        await ctx.send("오류가 발생하였습니다.")

bot.run(my_token)