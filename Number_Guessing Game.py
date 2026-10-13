import random

min = int(input("Enter the Lower Boundary for Your Guess Range : "))
max = int(input("Enter the Upper Boundary for Your Guess Range : "))
attemps = int(input("Enter the Number of Guess attemps : "))
count=0
while attemps!=count:
    try:
        number_to_Guess = random.randint(min,max)
        count += 1
        number=int(input(f"Enter a Number Between {min} and {max} : "))

        if number>max or number<min:
            print("Enter a number between the Range you Entered")
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

print(f"Total Attempts Reached and the Number to be guessed was:  {number_to_Guess}")