mark=int(input("enter your Mark : "))
if mark>=90:
    Grade="A+"
elif mark>=80:
    Grade="A"
elif mark>=75:
    Grade="A-"
elif mark>=70:
    Grade="B+"
elif mark>=65:
    Grade="B"
elif mark>=60:
    Grade="B-"
elif mark>=55:
    Grade="C+"
elif mark>=50:
    Grade="C"
elif mark>=45:
    Grade="C-"
elif mark>=40:
    Grade="D+"
elif mark>=30:
    Grade="D"
else:
    Grade="E"

print(Grade)

