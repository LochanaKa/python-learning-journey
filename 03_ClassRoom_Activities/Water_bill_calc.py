service_charge=150

def calc(units):
    if units<0:
        print("Invalid Input. Please Use a Positive Number!")
    else:
        if units <= 30:
            charge = units * 25
            print(f"Usage Charge Rs.{charge:.2f}")
            print(f"Total Bill Rs.{charge+service_charge:.2f}")
        elif units <= 50:
            charge = units * 40
            print(f"Usage Charge Rs.{charge:.2f}")
            print(f"Total Bill Rs.{charge+service_charge:.2f}")
        else:
            charge = units * 60
            print(f"Usage Charge Rs.{charge:.2f}")
            print(f"Total Bill Rs.{(charge+service_charge):.2f}")

try:
    units=int(input("\nEnter the No of Units: "))
    calc(units)

except ValueError:
    print("Enter a Valid Number")



