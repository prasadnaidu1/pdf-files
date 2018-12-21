import re
m=re.finditer("[python]","python is object oriented programming language")
for x in m:
    print("start:{}    end:{}   group:{}  ".format(x.start(),x.end(),x.group()))
