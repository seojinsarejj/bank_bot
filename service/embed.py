import asyncio, discord

class Embed:

    def my_transaction_embed(result):
         
        embed=discord.Embed(title="내 거래 내역", color=0x00ff56)

        minus = plus = 0

        for i in range(len(result)):
            minus += result[i][3]
            plus += result[i][4]
            embed.add_field(
                name=str(result[i][0]), 
                value= result[i][1] + " " + result[i][2]  + " " + str(result[i][3]) + " " + str(result[i][4]) + " " + str(result[i][5]) + " " + result[i][6],
                inline=False)

        embed.add_field(
            name="총 지출",
            value=str(format(minus, ","))
        )
        embed.add_field(
            name="총 수입",
            value=str(format(plus, ","))
        )

        return embed