#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: May 6, 2025
# This program uses a function that
# calculates the area of a triangle


def calculate_area(base, height):
    area = 1 / 2 * base * height
    print("The area is {} cm^2".format(area))


def main():
    base_string = input("Enter the base of a rectangle: ")
    try:
        base_integer = int(base_string)
        height_string = input("Enter the height of a rectangle: ")
        try:
            height_integer = int(height_string)
            calculate_area(base_integer, height_integer)
        except Exception:
            print("{} is not valid input".format(height_string))
    except Exception:
        print("{} is not valid inout".format(base_string))


if __name__ == "__main__":
    main()
