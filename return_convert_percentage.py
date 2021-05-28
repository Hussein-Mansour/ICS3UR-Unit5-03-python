#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Thu/May27/2021
# This program takes the level to grade and returns the middle percentage mark


def percentage_mark(percentage_int):
    # this function checks Which answer and prints it
    # process & output
    if percentage_int == 4:
        print(
            "\nlevel {0} has a middle percentage of 90%".format(percentage_int)
            )
    elif percentage_int == 3:
        print(
            "\nlevel {0} has a middle percentage of 74%".format(percentage_int)
            )
    elif percentage_int == 2:
        print(
            "\nlevel {0} has a middle percentage of 64%".format(percentage_int)
            )
    elif percentage_int == 1:
        print(
            "\nlevel {0} has a middle percentage of 54%".format(percentage_int)
            )
    return percentage_int


def level(level_from_user):
    # this function checks Which answer and prints it
    # process & output
    if level_from_user == "4+":
        print(
            "\nlevel {0} has a middle percentage of 97%"
            .format(level_from_user)
            )
    elif level_from_user == "4-":
        print(
            "\nlevel {0} has a middle percentage of 84%"
            .format(level_from_user)
            )
    elif level_from_user == "3+":
        print(
            "\nlevel {0} has a middle percentage of 78%"
            .format(level_from_user)
            )
    elif level_from_user == "3-":
        print(
            "\nlevel {0} has a middle percentage of 71%"
            .format(level_from_user)
            )
    elif level_from_user == "2+":
        print(
            "\nlevel {0} has a middle percentage of 68%"
            .format(level_from_user)
            )
    elif level_from_user == "2-":
        print(
            "\nlevel {0} has a middle percentage of 61%"
            .format(level_from_user)
            )
    elif level_from_user == "1+":
        print(
            "\nlevel {0} has a middle percentage of 58%"
            .format(level_from_user)
            )
    elif level_from_user == "1-":
        print(
            "\nlevel {0} has a middle percentage of 51%".
            format(level_from_user)
            )
    elif level_from_user == "R":
        print(
            "\nlevel {0} has a middle percentage of 0% - 49%"
            .format(level_from_user)
            )
    return level_from_user


def main():
    # this function gets length and width
    # input
    level_from_user = input(
        "Enter the level you want converted to a percentage: ")
    level(level_from_user)
    try:
        percentage_int = int(level_from_user)
        # call function
        percentage_mark(percentage_int)
    except Exception:
        print("\nInvalid Input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
