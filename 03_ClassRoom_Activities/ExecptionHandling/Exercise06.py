while True:
    try:
        n=int(input("Enter a number: "))
    except ValueError:
        print("Try Again!")
    else:
        print("Your Number is correct & it is",n)
        break

