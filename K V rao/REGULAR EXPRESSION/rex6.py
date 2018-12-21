import re
a=input("enter a main string : ")
b=input("enter searching  main string : ")
m1=re.findall(b,a)
print(m1)#no need to write group() function