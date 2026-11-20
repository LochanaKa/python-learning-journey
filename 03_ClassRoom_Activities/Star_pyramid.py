count=1
try:
    rows=int(input("Enter the No of Rows (1-9) : "))
    if rows <=0 or rows>9:
        print("Invalid Rows!. Please enter a number in (1-9) range")
    else:
        for row in range(1,rows+1):
            #print the spaces before this row's stars
            for space in range(rows-row):
                print(" ",end="")
            for star in range(2*row-1):
                print("*",end="")
            print()

except ValueError:
    print("Enter a Valid Number!")


