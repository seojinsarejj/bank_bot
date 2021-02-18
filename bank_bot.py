import asyncio, discord
from discord.ext import commands

from config import token
from service.crawling import Crawling
from service.statistics import Statistics
from service.utils import Util

my_token = token
game = discord.Game("도움말 : !도움말")



bot = commands.Bot(command_prefix='!', status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
    print('봇 시작')
 
 
@bot.command()
async def 거래내역(ctx,*param):
    await ctx.send("잠시만 기다려주세요")
    try:
        await ctx.send(embed=Statistics.my_transaction_embed(param[0],param[1]))  
    except Exception as e:
        print(e)
        await ctx.send("오류가 발생하였습니다.")


@bot.command()
async def 이상치(ctx):
    await ctx.send("잠시만 기다려주세요")
    try:
        await ctx.send(embed=Statistics.find_larger_than_usual_expenditure())

    except Exception as e:
        print(e)
        await ctx.send("오류가 발생하였습니다.")


@bot.command()
async def 잔액통계(ctx):
    await ctx.send("잠시만 기다려주세요")
    try:
        await ctx.send(file=Statistics.get_balance_graph())
    except Exception as e:
        print(e)
        await ctx.send("오류가 발생하였습니다.")


bot.run(my_token)