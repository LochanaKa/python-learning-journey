#DATA STRUCTURES

#LISTS
#Lists design specially to put the values of same Type
x=[1,23,58,589,5451]
print(x)

print("==============================")
#How to access elements in a list
y = x[0]
print(y) #Output is 1 because here it goes the index from 0

print("==============================")
#Changing the list value
x[1]=500
print(x)

print("==============================")
#Adding New Values
x.append(2)
print(x) #Adding new value at the end of the list

print("==============================")
#Adding new Value at a middle place
x.insert(2,6000)
print(x)

print("==============================")
#Removing a Element
x.remove(589)
print(x)

print("==============================")
#Removing Element by mentioning the index
x.pop(5)
print(x)

print("==============================")
#Addition of Lists
a=[25,54,87,95]
b=[2,25,8]
c=a+b
print(a)
print(b)
print(c)

print("==============================")
#Checking a value is there
print(x)
print(1 in x)
print(1 not in x)