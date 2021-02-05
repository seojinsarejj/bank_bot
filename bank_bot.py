import asyncio, discord
from discord.ext import commands

from config import token,account
from service.crawling import Crawling
from service.embed import Embed

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
        await ctx.send(embed=Embed.my_transaction_embed(result))
        
    except Exception as e:
        print(e)
        await ctx.send("오류가 발생하였습니다.")

bot.run(my_token)