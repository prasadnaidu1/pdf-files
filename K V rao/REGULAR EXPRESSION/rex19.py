
import re

while True:
    try:
        no=input("Enter a moble number :")
        if len(no)==10:
            mat=re.match("[6789]+\d+",no)
            if mat:
                print("valid mobile number")
                break
            else:
                print("invalid mobile number")
                ans=input("if you want to enter your mobile number press y :")
                if ans=="y":
                    continue
                else:
                    break
        else:
             print("enter 10 numbers only")

    except:
        print("Only numbers are allowed ")