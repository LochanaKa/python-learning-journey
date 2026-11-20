try:
    price=int(input("Enter the price: "))
except ValueError:
    print("Invalid price!")
else:
    print(f"Price Saved {price}")
print("done")