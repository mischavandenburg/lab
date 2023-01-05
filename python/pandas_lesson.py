import pandas

data = pandas.read_csv("weather_data.csv")

# pandas has two primary data structures, series and dataframes
# dataframe is the entire table, series is a column of that table

# turn the data to dict
data_dict = data.to_dict()

print(data_dict)

# turn the series to a list
temp_list = data["temp"].to_list()
print(temp_list)

# to get the average temperature, first I wrote this:

# average = 0
# for i in temp_list:
#     average += i
#
# print(average / len(temp_list))

# so dumb! much nicer example from the video:

print(sum(temp_list) / len(temp_list))

# now to use pandas:
# use the bracket notation to get hold of the column
print(data["temp"].mean())

# max temperature
print(data["temp"].max())

# alternative to temp, you can use the dot notation
print(data.temp)
print(data.condition)

# we've done series, but how to get rows?
# first get hold of the entire data table,
# then specify the row value you want to search for and return
# so the first data is the entire column, and you use the second part in []
# to access that particular row, like the key in the dict.
print(data[data.day == "Monday"])

# get out the row of data where temp was at max
max_temp = data.temp.max()
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp)

# use pandas.DataFrame(dictionary) to create a Data frame
# then you can use data.to_csv("my_csv_file.csv") to create csv file
