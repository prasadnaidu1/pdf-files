from itertools import permutations
perm = permutations(['1','2','3','a','b','c'])
user_input = input("Enter your desired character: ")
for i in list(perm):
    if i[0] == user_input:
        print(i)