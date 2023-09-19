from random import randint
computer_choice = randint(1,10)

user_choice = int(input("Hey try to guess my number !! "))

while user_choice != computer_choice:
    print(user_choice)
    print(computer_choice)
    user_choice = int(input("Try again: "))

print("You win!")
