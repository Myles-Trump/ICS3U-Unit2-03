#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program calculates the circumference of a circle
#    with both radius inputted by the user


import constants


def main():
    # this function calculates the circumference of a circle

    # input
    radius = int(input("Enter the radius (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("\nThe circumference of your circle is {0} mm."
          .format(circumference))


if __name__ == "__main__":
    main()
