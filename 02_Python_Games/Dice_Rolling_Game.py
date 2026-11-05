import random

count=0
#Loop
while True:
    # Ask: Roll the dice?

    choice = input("Roll the Dice? (y/n): ").lower()

    # If user enters y
    if choice == "y":
        n = int(input("Enter the number of Dice to Roll : "))
        count += 1
        if n<=0:
            print("Invalid Input!")
            continue

        dice = []

    #   Generate two random numbers
        for i in range(n):
            dice.append(random.randint(1,6))
    #   print them
        print(tuple(dice))

    # If the user enters n
    elif choice == "n":
    #   print thank you message
        print(f"Thank you for playing {count} times!")
    #   Terminate
        break
    # Else
    else:
        print("Invalid Choice!")
    #   Print Invalid choice
