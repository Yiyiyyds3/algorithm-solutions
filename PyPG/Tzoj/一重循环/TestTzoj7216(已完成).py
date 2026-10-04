flag=0
for i in range(5):
    pwd=input()
    if pwd=="Python@16":
        print("Login successful!")
        break
    elif flag==4:
        print("Input the password more than 5 times. Please reset your password by email!")
        break
    else:
        print("The password is wrong. Try again!")
        flag+=1
        
