try:
    divisor=int(input("Enter a Number: "))
    answer=12/divisor
    print(f"The Answer is {answer}")
except ValueError:
    print("Enter a Valid Number")
except ZeroDivisionError:
    print("Cannot devide zero")
print("Done")