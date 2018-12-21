count = 0
n = list(input().upper())
dic_count = {}
for i in n:
    if i not in dic_count.keys():
        dic_count[i] = 1
    else:
        dic_count[i] = dic_count[i] + 1
print(dic_count)  
print(dic_count['F']*'F' + dic_count['F']*'M')