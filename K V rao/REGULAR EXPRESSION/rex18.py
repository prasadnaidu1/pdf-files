import re

while True:
    try:
        str = input("enter a file name :")
        fp = open(str)
        ans = fp.read()
        rep = re.compile("[A-Z][a-z]+\d+[a-z]+")
        mat = rep.findall(ans)
        for x in mat:
            print(x)

        res2 = input("Do you want to continue  again press y:")
        if res2 == "y":
            continue
        else:
            break
    except:
        print("please enter valid input")

