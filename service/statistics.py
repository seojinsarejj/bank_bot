import asyncio, discord
import numpy as np
import json

from .utils import Util
from .crawling import Crawling

from config import account


class Statistics:

    # 거래  내역
    def my_transaction_embed(period, amount):

        my_id = account["id"]
        pw = account["pw"]

        crawling = Crawling(my_id, pw)
        result = crawling.get_transaction(period, amount)

        Util.write_json(period, amount, result)

        embed = discord.Embed(title="내 거래 내역", color=0x00FF56)

        minus = sum([i[3] for i in result])
        plus = sum([i[4] for i in result])

        row_len = len(result) if len(result) <= 23 else 23

        for i in range(row_len):

            name, value = Util.divide_date_and_contents(result[i])
            embed.add_field(name=name, value=value, inline=False)

        embed.add_field(name="총 지출", value=str(format(minus, ",")))
        embed.add_field(name="총 수입", value=str(format(plus, ",")))

        return embed

    # 평소보다 큰 지출
    def find_larger_than_usual_expenditure():

        period, amount, result = Util.read_json()

        embed = discord.Embed(title="평소보다 큰 지출", color=0x00FF56)

        value = [record[3] for record in result if record[3] != 0]
        q1, q3 = np.percentile(value, [25, 75])
        IQR = q3 - q1
        result = [record for record in result if record[3] < (q1 - 1.5 * IQR)]

        if result:

            row_len = len(result) if len(result) <= 23 else 23
            for i in range(row_len):
                name, value = Util.divide_date_and_contents(result[i])
                embed.add_field(name=name, value=value, inline=False)
        else:
            embed.add_field(name="평소보다 큰 지출이 없습니다.", value="X")

        return embed

    # 잔액 통계
    def get_balance_graph():

        period, amount, result = Util.read_json()

        df = Util.result_to_dataframe(result)
        df = df.sort_index(ascending=True)

        df_graph = df["balance"].plot(title="잔액 통계")
        fig = df_graph.get_figure()
        fig.savefig("file/balance.png")
        file = discord.File("file/balance.png")

        return file
