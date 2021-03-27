import pandas as pd
import json


class Util:
    def divide_date_and_contents(row):
        name = str(row[0])
        value = (
            row[1]
            + " "
            + row[2]
            + " "
            + str(row[3])
            + " "
            + str(row[4])
            + " "
            + str(row[5])
            + " "
            + row[6]
        )
        return name, value

    def result_to_dataframe(result):
        df = pd.DataFrame(
            result,
            columns=[
                "date",
                "sortation",
                "content",
                "minus",
                "plus",
                "balance",
                "dealership",
            ],
        )
        df.date = pd.to_datetime(df.date)
        df = df.set_index("date")

        return df

    def read_json():

        with open("file/data.json", "r", encoding="UTF-8") as f:
            json_data = json.load(f)

        period = json_data["data"]["period"]
        amount = json_data["data"]["amount"]
        result = json_data["data"]["result"]

        return period, amount, result

    def write_json(period, amount, result):

        json_data = dict()

        data = dict()

        data["period"] = period
        data["amount"] = amount
        data["result"] = result
        json_data["data"] = data

        with open("file/data.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent="\t", ensure_ascii=False)
