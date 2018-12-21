import re
m=re.finditer("[^python]","python is object oriented programming language")
no_of_occrs=0
for x in m:
    no_of_occrs+=1

    print("start:{}    end:{}   group:{}  ".format(x.start(),x.end(),x.group()))
print(no_of_occrs)