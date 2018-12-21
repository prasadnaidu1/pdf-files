import re
m1=re.finditer("p*","pythpponis opbjeppct orieppppnted lamgppppppuage")
for x in m1:
    print("start: {}    end: {}    group :{}  ".format(x.start(),x.end(),x.group()))

