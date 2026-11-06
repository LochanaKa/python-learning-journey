with open("attendence.txt", "a") as file:
    while True:
        userInput=input("Enter name to add (or 'e' to exit): ")

        if userInput.lower() == "e":
            break

        file.write(userInput+"\n")
        print(f"{userInput} added to attendence.txt")
