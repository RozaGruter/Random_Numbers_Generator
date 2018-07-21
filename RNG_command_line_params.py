import sys
import random as rd
import csv
import time


def get_data_types(nb_numbers):
    """
    What should be the data type for each number (1 - integer, 2 - float)
    Input
        nb_numbers -> how many numbers (int)
    Output
         data_type_per_number -> list of data types for each number
    """

    nb_type = input("Data Types (Enter 1 or 2 for each number, use space as a separator): ")
    print("")

    # split string
    data_types = nb_type.split(" ")
    allowed_data_types = (1, 2)
    data_nbr = len(data_types)

    if nb_numbers == data_nbr:
        try:
            for idx in range(data_nbr):
                if int(data_types[idx]) in allowed_data_types:
                    continue
                else:
                    raise ValueError

            # put splitted data into a list
            data_type_per_number = [int(data_types[i]) for i in range(data_nbr)]
            return data_type_per_number
        except ValueError:
            print("Invalid input. Please try again.")
            return get_data_types(nb_numbers)
    else:
        print("Invalid input. Please try again.")
        return get_data_types(nb_numbers)


def get_numbers_minmax(nb_numbers, data_types):
    """
    What are min & max values from which random numbers should be generated (for each number)
    Input:
        nb_numbers -> for how many numbers the details needs to be fetched
        data_types -> a list of data types (integers)
    Output:
        details_numbers -> a nested dictionary with info for each number
    """

    # create a nested dict with info for each number:
    # data type, min value, max value
    details_numbers = {"Number {}".format(idx + 1): {} for idx in range(nb_numbers)}
    numbers_minmax = []  # list of tuples

    for idx in range(nb_numbers):
        text = "Give min and max range of numbers for {}: ".format(idx + 1)
        number = get_number_minmax(text)  # tuple with min & max values for a given number
        numbers_minmax.append(number)

    # complete the nested dictionary with corresponding values for each number
    for idx in range(nb_numbers):
        details_numbers['Number {}'.format(idx + 1)] = {'data_type': data_types[idx], 'min': numbers_minmax[idx][0],
                                                        'max': numbers_minmax[idx][1]}

    return details_numbers


def get_number_minmax(txt):
    """
    A function to get one set of input (min & max) from the console
    Output
        number_minmax -> tuple of integers for min value and max value
    """

    number = input(txt)
    print("")
    number_splitted = number.split(" ")
    try:
        number_splitted_int = [int(number_splitted[i]) for i in range(len(number_splitted))]
        if number_splitted_int[0] < number_splitted_int[1]:
            number_minmax = tuple(number_splitted_int)
            return number_minmax
        else:
            raise ValueError
    except ValueError:
        print("Incorrect Input. Please try again.")
        return get_number_minmax(txt)


def number_data(data_type, min_val, max_val):
    """
    A function to generate the random number
    Input
        data_type -> int, type of output for the given number
        min_val -> minimum allowed value for this number
        max_val -> maximum allowed value for this number
    Output:
        number -> number output for the given iteration
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
        random_numbers -> a set of output of all the numbers
    Output:
        data is written into a csv file
    """

    with open(r'number_data.txt', 'a', encoding='utf8') as csvfile:
        number_writer = csv.writer(csvfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_NONE)
        number_writer.writerow(random_numbers)


def main(argv):
    """
    :return:
    """

    print(argv)

    try:
        if len(argv) != 3:
            raise IndexError
    except IndexError:
        print("Incorrect number of parameters. Script will terminate. Please try again.")
        sys.exit()

    try:
        if (int(argv[1]) > 6) or (int(argv[1]) <= 0):
            raise ValueError
        else:
            nbr = int(argv[1])
    except ValueError:
        print("Incorrect input for nb of numbers to generate. Script will terminate. Please try again.")
        sys.exit()

    try:
        refresh = int(argv[2])
    except ValueError:
        print("Incorrect input for refresh rate. Script will terminate. Please try again.")
        sys.exit()

    # nb_numbers = how_many_numbers()
    ref_rate = refresh
    data_types = get_data_types(nbr)
    numbers_min_max = get_numbers_minmax(nbr, data_types)

    while True:
        numbers = []
        for idx in range(nbr):
            tmp = numbers_min_max[f'Number {idx+1}']  # details of a given number (data type, min & max values)
            data = number_data(tmp['data_type'], tmp['min'], tmp['max'])
            numbers.append(data)
        write_into_csv(numbers)
        print(numbers)
        time.sleep(ref_rate)


if __name__ == '__main__':
    main(sys.argv[:])
