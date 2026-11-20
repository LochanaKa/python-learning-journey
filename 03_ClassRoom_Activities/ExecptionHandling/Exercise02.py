price=250

try:
    Tickets=int(input("Enter a number: "))
    print("No of Tickets: ",Tickets)
    print("Total Amount to pay: ",price*Tickets)
except ValueError:
    print("Use whole numbers")
print("Done")