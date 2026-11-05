quote ="She said, \"Hello!\""
path = "C:\\Users\\student"

print(quote)
print(path)

name="LochanaKarunarathna"
Module = "DS1102"
print("Student: " , name)
print("Module: ",Module)


print(len(name))
print(min(name))
print(max(name))
print(sorted(name))

text="python"

print(text+ "Lab")
print(text*2)
print(len(text))
print(max(text))

print(text[0:3])
print(text[0:5:2])
print(name[::-1])


word = "civic"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#
text1 = "Python java C++"
languages = text1.split(" ")
print(languages)

text2="\"CAT\""
for i in text2:
    print(i)

for i in range(len(text2)):
    print(i,text2[i])

text3 = "python Lab"
print(text3.casefold())
print(text3.islower())
print("hello".capitalize())
#

text4 = "My Python Programming"
print(text4.casefold())
print(text4.islower())
print(text4.count("a"))
print(text4.find("na"))
print(text4.endswith("na"))

title="MENU"
print(title.center(12, "-"))

item = "Book"
price = 1250
qty = 2
print(f"{qty} {item}s cost Rs. {price * qty}")


#
