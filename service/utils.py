class Util:

    def divide_date_and_contents(row):
        name = str(row[0])
        value = row[1] + " " + row[2]  + " " + str(row[3]) + " " + str(row[4]) + " " + str(row[5]) + " " + row[6]
        return name,value
