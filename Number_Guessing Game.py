import random

number_to_Guess=random.randint(1,100)
while True:
    try:
        number = int(input("Guess the number between 1 and 100 : "))
        if number <= 0 or number > 100:
            print("Enter a valid Number")
            continue

        if number > number_to_Guess:
            print("Too High")
        elif number < number_to_Guess:
            print("Too Low")
        else:
            print("Congratulations! You Guessed the Number")
            break
    except ValueError:
        print("Please Enter a Valid Input")

