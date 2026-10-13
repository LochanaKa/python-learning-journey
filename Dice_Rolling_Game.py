import random

#Loop
while True:
    # Ask: Roll the dice?
    choice = input("Roll the Dice? (y/n): ").lower()
    # If user enters y
    if choice == "y":
    #   Generate two random numbers
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
    #   print them
        print(f'{dice1},{dice2}')
    # If the user enters n
    if choice == "n":
    #   print thank you message
        print("Thank you for playing")
    #   Terminate
        break
    # Else
    else:
        print("Invalid Choice!")
    #   Print Invalid choice
