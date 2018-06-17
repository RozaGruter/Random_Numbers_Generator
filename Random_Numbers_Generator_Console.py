#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:26:18 2018

@author: roza.gruter
"""

import random as rd
import csv
import time


def get_nb_sensors():
    """
    Ask user how many sensors need to be generated
    Output:
        nb_sensors -> number of sensors requested by the user
    """

    print("****************************************************************")
    print(" Enter the number of sensors to be generated.")
    print(" You can choose between 1 and 6 sensors.")
    nb_sensors = input("Nb of sensors: ")
    print("")
    print("****************************************************************")

    try:
        if (int(nb_sensors) > 6) or (int(nb_sensors) <= 0):
            raise ValueError
        else:
            return int(nb_sensors)
    except ValueError:
        print("Incorrect input. Please try again.")
        return get_nb_sensors()


def get_refresh_rate():
    """
    What should be the refresh rate (in seconds)
    Output:
        --> integer, nb of seconds between refresh
    """

    refresh_rate = input("Enter the refresh rate (in seconds): ")
    print("")
    print("****************************************************************")

    try:
        return int(refresh_rate)
    except ValueError:
        print("Incorrect input. Please try again.")
        return get_refresh_rate()


def get_data_types(nb_sensors):
    """
    What should be the data type for each sensor (1 - integer, 2 - float)
    Input
        nb_sensors -> how many sensors (int)
    Output
         data_type_per_sensor -> list of data types for each sensor
    """

    print("Choose data type for each sensor: 1-integer / 2-float")
    print("Enter 1 or 2 for each sensor, use space as a separator")
    nb_type = input("Data Types: ")
    print("")
    print("****************************************************************")

    # split string
    data_types = nb_type.split(" ")
    allowed_data_types = (1, 2)
    data_nbr = len(data_types)

    if (nb_sensors == data_nbr):
        try:
            for idx in range(data_nbr):
                if int(data_types[idx]) in allowed_data_types:
                    continue
                else:
                    raise ValueError

            # put splitted data into a list
            data_type_per_sensor = [int(data_types[i]) for i in range(data_nbr)]
            return data_type_per_sensor
        except ValueError:
            print("Invalid input. Please try again.")
            return get_data_types(nb_sensors)
    else:
        print("Invalid input. Please try again.")
        return get_data_types(nb_sensors)


def get_sensors_minmax(nb_sensors, data_types):
    """
    What are min & max values from which random numbers should be generated (for each sensor)
    Input:
        nb_sensors -> for how many sensors the details needs to be fetched
        data_types -> a list of data types (integers)
    Output:
        details_sensors -> a nested dictionary with info for each sensor
    """

    # create a nested dict with info for each sensor:
    # data type, min value, max value
    details_sensors = {"Sensor {}".format(idx + 1): {} for idx in range(nb_sensors)}
    sensors_minmax = []  # list of tuples

    for idx in range(nb_sensors):
        print("Give min and max range of numbers for sensor {}:".format(idx + 1))
        sensor = get_sensor_minmax()  # tuple with min & max values for a given sensor
        sensors_minmax.append(sensor)

    # complete the nested dictionary with corresponding values for each sensor
    for idx in range(nb_sensors):
        details_sensors['Sensor {}'.format(idx + 1)] = {'data_type': data_types[idx], 'min': sensors_minmax[idx][0],
                                                        'max': sensors_minmax[idx][1]}

    return details_sensors


def get_sensor_minmax():
    """
    A function to get one set of input (min & max) from the console
    Output
        sensor_minmax -> tuple of integers for min value and max value
    """

    sensor = input()
    print("")
    print("****************************************************************")
    sensor_splitted = sensor.split(" ")
    try:
        sensor_splitted_int = [int(sensor_splitted[i]) for i in range(len(sensor_splitted))]
        if sensor_splitted_int[0] < sensor_splitted_int[1]:
            sensor_minmax = tuple(sensor_splitted_int)
            return sensor_minmax
        else:
            raise ValueError
    except ValueError:
        print("Incorrect Input. Please try again.")
        return get_sensor_minmax()


def sensor_data(data_type, min_val, max_val):
    """
    A function to generate the random number
    Input
        data_type -> int, type of output for the given sensor
        min_val -> minimum allowed value for this sensor
        max_val -> maximum allowed value for this sensor
    Output:
        number -> sensor output for the given iteration
    """

    if data_type == 1:
        number = rd.randint(min_val, max_val)
        return number
    elif data_type == 2:
        number = float("{0:.2f}".format(rd.uniform(min_val, max_val)))
        return number


def write_into_csv(random_numbers):
    """
    A function to write each set of random data into one line in a csv file.
    The file will be created if doesn't exist, or new data will be added if already exist.
    Input
        random_numbers -> a set of output of all the sensors
    Output:
        data is written into a csv file
    """

    with open(r'sensor_data.txt', 'a', encoding='utf8') as csvfile:
        sensor_writer = csv.writer(csvfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_NONE)
        sensor_writer.writerow(random_numbers)


def main():
    """
    Main function to run the generator
    Manages obtaining input values from the user, generating data in a given time interval and writing it into a file
    """
    nb_sensors = get_nb_sensors()
    ref_rate = get_refresh_rate()
    data_types = get_data_types(nb_sensors)
    sensors_min_max = get_sensors_minmax(nb_sensors, data_types)

    while True:
        sensor_numbers = []
        for idx in range(nb_sensors):
            tmp = sensors_min_max[f'Sensor {idx+1}']  # details of a given sensor (data type, min & max values)
            data = sensor_data(tmp['data_type'], tmp['min'], tmp['max'])
            sensor_numbers.append(data)
        write_into_csv(sensor_numbers)
        print(sensor_numbers)
        time.sleep(ref_rate)


if __name__ == '__main__':
    main()
