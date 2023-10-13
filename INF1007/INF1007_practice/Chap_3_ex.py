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


def convertir_degree_radians(degree, minute, secondes):
    sec_degree = degree*60*60 
    sec_minute = minute*60 
    
    radians = (sec_degree + sec_minute + secondes)/206265

    return radians

#print(convertir_degree_radians(1,0,0))


# 4/
def convertir_radians_degree(radian):
    total_degree = radian*(180/math.pi)
    
    degree_entier = int(total_degree)

    total_minute_left = abs(total_degree - degree_entier) * 60

    minute_entier = int(total_minute_left)

    total_seconds_left = abs(total_minute_left - minute_entier) * 60

    seconds_entier = int(total_seconds_left)

    return degree_entier, minute_entier, seconds_entier

#print(convertir_radians_degree(0.994838))

#5

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
    
#bill_return_calculator()