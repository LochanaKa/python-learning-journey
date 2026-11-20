count=0
sum=0

try:
    integer = int(input("\nEnter a Integer: "))
    if integer <=0:
        print("Invalid Number!")
    else:
        str_int=str(integer)
        for digit in str_int:
            count+=1
            sum=sum+int(digit)
        print("\nDigits " ,count)
        print("Digit Sum " , sum )
        print("Reversed ", str_int[::-1])

except ValueError:
    print("Enter a Valid Input!")