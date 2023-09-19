from random import randint
computer_choice = 8

user_choice = int(input("Hey try to guess my number !! " ))

bool1 = user_choice == computer_choice

while user_choice != computer_choice:
    user_choice = input("Hey try to guess my number !! " )
    print(user_choice)
    print(computer_choice)
    if user_choice == computer_choice:
        break
    
print("you win")
