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
    #weather data is integers/strings and floats. I need to convert these to integers?
    #print(find_min([1,2,3])) #call the function that you are creating, print it (and then delete after it working)
    # weather = float(weather_data)
    # print(find_min([1,2,3]))
    if not weather_data:
        return None, None
    
    min_value = weather_data[0]
    min_index = 0

    for index, value in enumerate(weather_data):
        if value <= min_value:
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
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
