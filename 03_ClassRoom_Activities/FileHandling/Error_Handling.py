try:
    with open("Rice.txt","r") as file:
        rice=file.read()
        print(rice)
except FileNotFoundError:
    print("Error: File not found මචන්")
