# # with open(file="weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# import csv
# with open(file="weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
#
#
# # how to get data in a row
#
# monday = data[data.day == "Monday"]
#
# print(monday.temp)
#
#
# data_dict = {
#     "students" : ["Parthit", "Ria", "Arefa", "Karan", "Rajat"],
#     "scores" : [100, 99, 100, 77, 98]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data.to_csv('new_data.csv'))

# import pandas
# data = pandas.read_csv("squirrel.csv")
#
#
# df = data['Primary Fur Color'].value_counts()
# print(df.to_csv('colors_of_squirrel_output.csv'))

