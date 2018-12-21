import re
a=input("enter a  original string : ")
b=input("enter a  existiting string : ")
c=input("enter a  replacing string : ")
m1=re.sub(b,c,a)
print(m1)
