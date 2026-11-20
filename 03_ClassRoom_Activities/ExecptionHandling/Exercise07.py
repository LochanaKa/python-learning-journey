def to_minutes(hours):
    if hours <= 0 :
        raise ValueError("Hours cannot be negative")
    return hours*60

try:
    n=int(input("Enter Hours: "))
    print(to_minutes(n))
except ValueError as error:
    print(error)