try:
    Tickets=int(input("Enter a number: "))
    print("Tickets: ",Tickets)
except ValueError:
    print("Use whole numbers")
print("Done")