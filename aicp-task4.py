import math


def calcAreaHexagon(side_length):
    return round(1.5 * 1.732 * side_length * side_length, 2)

def calcPeriHexagon(side_length):
    return round(6 * side_length, 2)

def calcAngleSumHexagon():
    return 6 * 120

def displayHexagon(side_length):
    print(f"Area of hexagon is: {calcAreaHexagon(side_length)}")
    print(f"Perimeter of hexagon is: {calcPeriHexagon(side_length)}")
    print(f"Sum of angles of hexagon is: {calcAngleSumHexagon()}")

def calcAreaSquare(side_length):
    return round(side_length * side_length, 2)

def calcPeriSquare(side_length):
    return round(4 * side_length, 2)

def displaySquare(side_length):
    print(f"Area of Square is: {calcAreaSquare(side_length)}")
    print(f"Perimeter of Square is: {calcPeriSquare(side_length)}")

cnic_last_digit = int(input("Enter the last digit of your CNIC: "))

hexagon_side_length = cnic_last_digit
square_side_length = cnic_last_digit + 1

while True:
    print("\nEnter 1 to calculate area, perimeter, and sum of angles of hexagon")
    print("Enter 2 to calculate area and perimeter of square")
    print("Press any other key to exit")
    choice = input("Enter here: ")

    if choice == '1':
        displayHexagon(hexagon_side_length)
    elif choice == '2':
        displaySquare(square_side_length)
    else:
        print("Program terminated.")
        break
