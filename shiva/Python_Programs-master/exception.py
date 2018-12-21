''' Exception handling<br>

We have been asking Somu to enter product count and what if product count is entered as "10 no" which is not a number, your program may fail. <br>

What if we are trying to get a product cost from list or dictonary and product is not available it will throw an error <br>

Take one of Somu billing program and add exception handling, if there is no exception, say Thank you for using the system. Even if exception is there or not ask him for feedback(input). '''

product_list=['A','B','C','Others']
product_list_cost=[10,20,30,30]
try:
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
except Exception as inst:
    print("Exception",type(inst),inst)
else:
    print("Thank you for using the system.")
finally:
    feedback = input("Enter your feedback: ")
#hai