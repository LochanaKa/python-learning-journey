price=float(input("\nEnter the price of the book: "))
copies=int(input("Enter the No. of Books: "))
discountP=float(input("Enter the Discount Percentage: "))


total = price*copies
discount=(total*(discountP/100))
subtotal=total-discount
print(f"\nThe Total is : Rs.{total:.2f}")
print(f"The Discount is : Rs.{discount:.2f}")
print(f"The Subtotal is : Rs{subtotal:.2f}")