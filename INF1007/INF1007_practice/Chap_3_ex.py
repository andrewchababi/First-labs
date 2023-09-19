# 1/ Write a progam that calculates the square root of a number and its square
import math

def square_and_root(number):
    square = number**2
    root = math.sqrt(number)
    print(square,root)

#square_and_root(7)

# 2/ Write a program that takes the average of three number 

def average_calculate(num1, num2, num3):
    average = (num1+num2+num3)/3
    print(average)

#average_calculate(5,10,15)

# 3/ write a program that turns an angle in radiants to degrees then minutes then seconds
#this was wrong you were supposed to make it intake a angle in degrees, minuts, seconds and output in rads


def angle_converter():
    degrees = float(input("degrees "))
    minutes = float(input("minutes "))
    seconds = float(input("seconds "))
    raw_degrees = degrees + minutes/60 + seconds/3600
    rad_angle = 5
    
#angle_converter(6)

# 4/

def bill_return_calculator():
    whole_number = float(input("what is the amount you wish to be returned "))
    bill_100 = whole_number//100
    rest = whole_number%100
    bill_20 = rest//20
    rest = rest % 20
    bill_10 = rest//10
    rest = rest % 10
    bill_5 = rest // 5
    rest = rest % 5 
    bill_1 = rest // 1
    
    print(f"Here is your {whole_number} in {bill_100} hundred dollar bills, "
          f"{bill_20} twenty dollar bills, {bill_10} ten dollar bills, "
          f"{bill_5} five dollar bills, and {bill_1} one dollar bills.")
    
bill_return_calculator()