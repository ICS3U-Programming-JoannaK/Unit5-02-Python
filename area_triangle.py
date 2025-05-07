#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: May 6, 2025
# This program uses a function that
# calculates the area of a triangle


def calculate_area(length, width):
    area = length * width
    print("The area is {} cm^2".format(area))


def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    print("The perimeter is {}cm".format(perimeter))


def main():
    length_string = input("Enter the length of a rectangle: ")
    try:
        length_integer = int(length_string)
        width_string = input("Enter the width of a rectangle: ")
        try:
            width_integer = int(width_string)
            calculate_area(length_integer, width_integer)
            calculate_perimeter(length_integer, width_integer)
        except Exception:
            print("{} is not valid input".format(width_string))
    except Exception:
        print("{} is not valid inout".format(length_string))


if __name__ == "__main__":
    main()
