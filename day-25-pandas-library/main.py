# with open("day-25-pandas-library/weather_data.csv") as f:
#    data = f.readlines()
#    print(data)

# import csv

# with open("day-25-pandas-library/weather_data.csv") as f:
#     data = csv.reader(f)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
         

import pandas

data = pandas.read_csv("day-25-pandas-library/weather_data.csv")
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp)
# print(data[data.temp == data.temp.max()].day)

# mon_temp = data[data.day == "Monday"].temp[0]

# farenheit = (mon_temp * 9/5) + 32

# print(farenheit)

