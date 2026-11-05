import datetime

nic = input("Enter the NIC No: ")

year = int(nic[0:4])
day = int(nic[4:7])

if day>500:
    gender="Female"
    day = day-500
else:
    gender="Male"

dob = datetime.date(year, 1, 1) + datetime.timedelta(days=day - 1)
today= datetime.date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age = age-1

print("Date of Birth: ", dob)
print("Age: ", age)
print("Gender: ", gender)