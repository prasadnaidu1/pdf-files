import  re
a=input("enter a main string :  ")
b=input("enter searching string :")
m1=re.search(b,a)
print(m1.group())