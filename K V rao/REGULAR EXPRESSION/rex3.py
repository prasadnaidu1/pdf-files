import re
a=input("enter a original string")
b=input("enter for searching string :")
m1=re.match(b,a)
print(m1.group())