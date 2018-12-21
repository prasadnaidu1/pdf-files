import re
data=re.compile("\d{10}")
while True:
    no=input("Enter a moble number :")
    if len(no)==10:
        mat=data.search(no)
        if mat:
            print("valid mobile number")
            break
        else:
            print("invalid mobile number")
    else:
        print("enter 10 numbers only")





