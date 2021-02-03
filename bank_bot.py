import asyncio, discord
from discord.ext import commands

from config import token,account
from service.crawling import Crawling


my_id = account['id']
pw = account['pw']
my_token = token
print(my_token)
game = discord.Game("도움말 : !도움말")

crawling = Crawling(my_id,pw)

bot = commands.Bot(command_prefix='!', status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
    print('봇 시작')


@bot.command()
async def 거래내역(ctx):
    
    embed=discord.Embed(title="내 거래 내역", color=0x00ff56)
    result = crawling.get_transaction(3,50)
    for i in range(len(result)):
        embed.add_field(
            name=str(result[i][0]), 
            value= result[i][1] + " " + result[i][2]  + " " + str(result[i][3]) + " " + str(result[i][4]) + " " + str(result[i][5]) + " " + result[i][6],
            inline=False)

    await ctx.send(embed=embed)

bot.run(my_token)