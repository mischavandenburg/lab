from icecream import ic
import pandas

# add 1 to each item in list
numbers = [1, 2, 3]
new_numbers = [i + 1 for i in numbers]

# take 1 to 4 and double each number
double = [i * 2 for i in range(1, 5)]

# conditional list comprehension
double = [i * 2 for i in range(1, 5) if i > 2]

# squared numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared = [i * i for i in numbers]

# filter even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [i for i in numbers if i % 2 == 0]

# dictionary comprehensions


# create a new dictionary that counts the
# number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# make a list of words
words = [word for word in sentence.split()]
result = {word: len(word) for word in words}

# take each temperature and convert to fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: ((temp * 9/5) + 32) for (day, temp) in weather_c.items()}
