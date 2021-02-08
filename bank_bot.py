import asyncio, discord
from discord.ext import commands

from config import token,account
from service.crawling import Crawling
from service.statistics import Statistics
from service.utils import Util

import pandas as pd
import matplotlib.pyplot as plt



my_id = account['id']
pw = account['pw']
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
        crawling = Crawling(my_id,pw)
        result = crawling.get_transaction(int(param[0]),int(param[1]))
        await ctx.send(embed=Statistics.my_transaction_embed(result))
        
    except Exception as e:
        print(e)
        await ctx.send("오류가 발생하였습니다.")


@bot.command()
async def 이상치(ctx,*param):
    await ctx.send("잠시만 기다려주세요")
    try:
        crawling = Crawling(my_id,pw)
        result = crawling.get_transaction(int(param[0]),int(param[1]))
        await ctx.send(embed=Statistics.find_larger_than_usual_expenditure(result))

    except Exception as e:
        print(e)
        await ctx.send("오류가 발생하였습니다.")


@bot.command()
async def 잔액통계(ctx,*param):
    await ctx.send("잠시만 기다려주세요")
    try:
        crawling = Crawling(my_id,pw)
        result = crawling.get_transaction(int(param[0]),int(param[1]))
        await ctx.send(file=Statistics.get_balance_graph(result))

    except Exception as e:
        print(e)
        await ctx.send("오류가 발생하였습니다.")


bot.run(my_token)