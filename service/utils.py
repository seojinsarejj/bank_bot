
import pandas as pd
class Util:

    def divide_date_and_contents(row):
        name = str(row[0])
        value = row[1] + " " + row[2]  + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " " + row[6]
        return name,value


    def result_to_dataframe(result):
        df = pd.DataFrame(result,columns=['date','sortation','content','minus','plus','balance','dealership'])
        df.date = pd.to_datetime(df.date)
        df = df.set_index('date')

        return df