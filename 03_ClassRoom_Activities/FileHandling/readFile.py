with open("reminder.txt", "r") as file:
    text = file.read()
print(text, end="")

with open("names.txt", "r") as file:
    names = file.readline()