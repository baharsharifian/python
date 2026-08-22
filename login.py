
correct_username = "root"
correct_password = "123"

attempt=0

while attempt < 3:
    username = input("enter username : ")
    password = input("enter password : ")
    if username == correct_username and password == correct_password:

        print ("Login Successful")
        break
    else:
        print("username or password is wrong")
        attempt += 1

if attempt >= 3:
        print ("account lock")

