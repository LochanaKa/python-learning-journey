def grade(mark):
 if mark>=75:
     return "A"
 elif mark>=50:
     return "B"
 elif mark>=25:
     return "C"
 else:
     return "D"


grade = grade(85)
print(grade)
