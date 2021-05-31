#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Thu/May27/2021
# This program takes the level to grade and returns the middle percentage mark


def level(percentage_str):
    # this function checks Which answer and prints it
    # process & output

    if percentage_str == "4":
        percentage_str = 90
    elif percentage_str == "3":
        percentage_str = 75
    elif percentage_str == "2":
        percentage_str = 64
    elif percentage_str == "1":
        percentage_str = 54
    elif percentage_str == "4+":
        percentage_str = 97
    elif percentage_str == "4-":
        percentage_str = 84
    elif percentage_str == "3+":
        percentage_str = 78
    elif percentage_str == "3-":
        percentage_str = 71
    elif percentage_str == "2+":
        percentage_str = 68
    elif percentage_str == "2-":
        percentage_str = 61
    elif percentage_str == "1+":
        percentage_str = 58
    elif percentage_str == "1-":
        percentage_str = 51
    elif percentage_str == "R":
        percentage_str = 49

    return percentage_str


def main():
    # this function this function call other functions
    # input
    level_from_user = input(
        "Enter the level you want converted to a percentage: ")
    try:
        percentage_str = level_from_user
        # call function
        some_var = level(percentage_str)
        print(
            "\nlevel {0} has a middle percentage of {1}%"
            .format(level_from_user, some_var)
            )
    except Exception:
        print("\nInvalid Input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
