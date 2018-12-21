''' Take the billing system program and rewrite it using 2 data structures as 
products_list, Product_cost_list 
Where ever you are accessing product names and costs you should use lists '''

import sys
product_list=['A','B','C','Others']
product_list_cost=[10,20,30,30]
num_prod_a= int(input("How Many product A?:"))
num_prod_b= int(input("How many product B?:"))
num_prod_c= int(input("How Many product C?:"))
num_prod_other= int(input("How Many product Other?:"))
amount = num_prod_a * product_list_cost[0] + num_prod_b * product_list_cost[1] + num_prod_c * product_list_cost[2] + num_prod_other * product_list_cost[3]
discount_amount = (amount*10)/100
bill_amount = amount - discount_amount
print("Your bill before discount:",amount)
print("Final Bill Amount:",bill_amount)
print("You saved amount:",discount_amount)