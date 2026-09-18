admin="lochana"
pwd="123456"
count=0
login_successful=False

while count<=2:
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    count = count + 1
    if username==admin:
        if pwd==password:
            print("Login Successful")
            login_successful = True
            break
        else:
            print("Wrong Password")
    else:
        print("Unknown User Try Again")
if login_successful==False:
    print("Access Denied!!")