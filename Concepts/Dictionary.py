#Dictionary has key value pair

#As a ethic use keys in same type

#In dictionary we can't call values as index calling system of lists because in a dictionary although we see that a order the values are not in a order

#Here we do not need to have in same Type as Lists

#Initialization of a dictionary
x={"Name":"Lochana","Age":21,"City":"Kurunegala"}
print(x)

print("==============================")
#After craeting a Dictionary adding a value
x["Country"]="SriLanka"
print(x)

print("==============================")
#Changing a Data
x["Name"]="Kamal"
print(x)

print("==============================")
#Getting Keys of the dictionary
print(x.keys())
#Getting the Values of the dictionary
print(x.values())

print("==============================")
#We can add a list in side a key of value
#Although the key is a single value but the values are not
print(x)
x["City"]=["Kurunegala","Sabra"]
print(x)
