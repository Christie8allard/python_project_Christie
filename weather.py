import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"
print(format_temperature(120))

#what i'm passing is a string type. 

# print(format f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")
    #FUNCTION RETURNING "NONE' its either not returning. The assertionError tells you what you should be returning e.g  (57.0, 1)



def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    num2 =float(temp_in_fahrenheit)
    # print(type(num2))
    # print(num2+1)
    # print (temp_in_fahrenheit,type(temp_in_fahrenheit))
    celsius = (num2 - 32) * 5 / 9
    # print(celsius,type(celsius))
    formatted_value = float("{:.1f}".format(celsius))
    # print(formatted_value,type(formatted_value))
    return formatted_value


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total = 0
    for data in weather_data:
        # print(data)
        data = float(data)
        # print(data)
        total += data

    return total / len(weather_data)

# print(calculate_mean(["51", "58", "59", "52", "52", "48", "47", "53"]))


import csv
def load_data_from_csv(csv_file): #read Csv file
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    #want to read file
    #for every row of data make a list (but skip the header row first)
    #ensure empty rows don't get a list
    data = []
    with open(csv_file, mode='r',) as file:
        csv_reader = csv.reader(file)
        # how do I pull the data here?
        for i, row in enumerate(csv_reader):
            #print(i)
            if row:
                if i == 0:
                    continue
                data.append(row)
                #print(row)
                row[1] = int(row[1])
                row[2] = int(row[2]) #conter 2 elemtn at end to ints. for loop of data.
        #data.pop(0)  
    return data

#     csv_file = data(files)
#     with open(csv_file, mode="r") as files:
#         data = []
#         for row in csv_file:
#             print(row)

    


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    variable_index = 0 #whatever this number is identifies the order in the list
    if not weather_data: #if there's nothing to see in the list return nothing
        return ()
    
    for x in weather_data:
        #print(x,type(x)) - this will show me if I have strings, ints etc. 
        weather_data[variable_index] = float(x) #for every element in the list we define the type and make it a float
        variable_index = variable_index+1 #we're creating a variable index to keep track of the index that we're modifying as we go
    #for x in weather_data:
        #print(x,type(x))
    
    min_value = weather_data[0]
    min_index = 0

    for index, value in enumerate(weather_data):
        if value <= min_value: #will change to the last occurance 
            min_value = value
            min_index = index
    return min_value, min_index


def find_max(weather_data):  
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    variable_index = 0
    if not weather_data:
        return ()
    
    for x in weather_data:
        weather_data[variable_index] = float(x)
        variable_index = variable_index+1

    max_value = float('-inf') #ensures first number on list always larger. Better than zero if your data includes negitives.
    max_index = -1

    for index, value in enumerate(weather_data):
            if value >= max_value:
                max_value = value
                max_index = index
    return max_value, max_index



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # iterate over list of lists
    # have a string that you add to ech iteration
    # use fuctions to convert f to c and date format (within iteration)
    # make format daily summary (within iteration)
    # return daily summary after for loop
    num_of_days = len(weather_data)
    # print(num_of_days)
    # weather_min = find_min()
    # weather_min= (convert_f_to_c(the_min))
    # weather_max= (convert_f_to_c(the_max))
    min_list = []
    for row in weather_data:
        min_value = row[1]
        min_list.append(min_value)
    min_value, min_position =find_min(min_list)  
    cel_min_value = convert_f_to_c(min_value)
    # print(weather_data)
    # print(min_position)
    # print(weather_data[min_position][0])
    min_day = convert_date(weather_data[min_position][0])

    max_list = []
    for row in weather_data:
        max_value = row[2]
        max_list.append(max_value)
    max_value, max_postion = find_max(max_list)
    max_day = convert_date(weather_data[max_postion][0])
    cel_max_value = convert_f_to_c(max_value)

    min_average = convert_f_to_c(calculate_mean(min_list))
    max_average = convert_f_to_c(calculate_mean(max_list))

    return f"{num_of_days} Day Overview\n  The lowest temperature will be {cel_min_value}°C, and will occur on {min_day}.\n  The highest temperature will be {cel_max_value}°C, and will occur on {max_day}.\n  The average low this week is {min_average}°C.\n  The average high this week is {max_average}°C.\n"


    # daily_sum(converted_date,weather_min, weather_max)

# print(generate_summary( [
#             ["2020-06-19T07:00:00+08:00", -47, -46],
#             ["2020-06-20T07:00:00+08:00", -51, 67],
#             ["2020-06-21T07:00:00+08:00", 58, 72],
#             ["2020-06-22T07:00:00+08:00", 59, 71],
#             ["2020-06-23T07:00:00+08:00", -52, 71],
#             ["2020-06-24T07:00:00+08:00", 52, 67],
#             ["2020-06-25T07:00:00+08:00", -48, 66],
#             ["2020-06-26T07:00:00+08:00", 53, 66]
#         ]))

# 8 Day Overview
#   The lowest temperature will be -46.7°C, and will occur on Tuesday 23 June 2020.
#   The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
#   The average low this week is -16.1°C.
#   The average high this week is 12.4°C.




def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summaries = ""
    for day in weather_data:
        date = "---- " + convert_date(day[0]) + " ----"
        min_temp = format_temperature(convert_f_to_c(day[1]))
        max_temp = format_temperature(convert_f_to_c(day[2]))
        summary = f"{date}\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"
        daily_summaries += summary
    return daily_summaries
