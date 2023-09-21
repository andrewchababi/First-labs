"""from random import randint
computer_choice = randint(1,10)

user_choice = int(input("Hey try to guess my number !! "))

while user_choice != computer_choice:
    print(user_choice)
    print(computer_choice)
    user_choice = int(input("Try again: "))

print("You win!")

numbre = 5
result = 1

for i in range(numbre, 1, -1):
    result *= i

print(result)"""

text = "Le fermier élevait efficacement de magnifiques fleurs près de l'effigie."
words = text.split()
numbre_of_e = 0
numbre_of_f = 0
numbre_of_words = 0

for word in words:
    if word.count("e") >= 2 and "f" in word:
        numbre_of_words += 1
print(numbre_of_words)


