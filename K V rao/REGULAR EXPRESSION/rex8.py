a=[10,30,52,2,67,50,59]
p=a.sort()
print(a)
print(p)

while True:
    try:
        no = int(input("enter a  index number : "))
        if a[no]<=0:
            print("You entered valid input")
            print("Your expected  number is :",a[no])

            continue
        elif a[no]>=1:
            print("You entered valid input")
            print("Your expected index number is :", a[no])
            continue
        else:
            print("invalid input")
            break
    except:
        print("You Entered Charcters; Enter only Digits either Possitive or Negitive ")
        ans=input("To you want one more time  press y :")
        if ans=="y":
            continue
        else:
            break
    finally:
        print("Thanks You ")






























