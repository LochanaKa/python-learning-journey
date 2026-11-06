count=0
with open("names.txt", "r") as file:
    for line in file:
        count += 1

print("Total Count of Names : ",count)