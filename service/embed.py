import asyncio, discord
import numpy as np
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

    def find_larger_than_usual_expenditure(result):

        embed = discord.Embed(title="평소보다 큰 지출",color=0x00ff56)

        value = [record[3] for record in result if record[3] != 0]
        q1 , q3 = np.percentile(value, [25,75])
        IQR = q3 - q1
        result = [record for record in result if record[3] < (q1 - 1.5 * IQR)]

        if result :
            for i in range(len(result)):
                embed.add_field(
                    name=str(result[i][0]), 
                    value= result[i][1] + " " + result[i][2]  + " " + str(result[i][3]) + " " + str(result[i][4]) + " " + str(result[i][5]) + " " + result[i][6],
                    inline=False)
        else:
            embed.add_field(
                name= "평소보다 큰 지출이 없습니다.",
                value="X"
            )

        return embed