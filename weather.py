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
    print(celsius,type(celsius))
    formatted_value = float("{:.1f}".format(celsius))
    print(formatted_value,type(formatted_value))
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
        for row in csv_reader:
            if row:
                data.append(row)
                # row[1] = int(row[1]) conter 2 elemtn at end to ints. for loop of data.
        data.pop(0)
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

    min_value = weather_data[0]
    min_index = 0

    for index, value in enumerate(weather_data):
            if value <= min_value:
                min_value = value
                min_index = index




def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    #reads what's in the file
    #returns a list of the types of items in the file?
    daily_summaries = ""
    if len(weather_data) > 0:
        overview = f"{len(weather_data)}"
        min_temp, min_index = find_min([day[1] for day in weather_data])
        max_temp, max_index = find_max([day[2] for day in weather_data])
        average_low = calculate_mean(day[1] for day in weather_data)
        average_high = calculate_mean(day[2] for day in weather_data)
        min_day = convert_date(weather_data[min_index][0])
        max_day = convert_date(weather_data[max_index][0])
        daily_summaries += f"{overview} Day Overview\n"
        daily_summaries += f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {min_day}.\n"
        daily_summaries += f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {max_day}.\n"
        daily_summaries += f"  The average low this week is {format_temperature(convert_f_to_c(average_low))}.\n"
        daily_summaries += f"  The average high this week is {format_temperature(convert_f_to_c(average_high))}.\n"
    return daily_summaries



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
