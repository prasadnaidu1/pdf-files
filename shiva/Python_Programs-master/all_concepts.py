'''Does this program work in real world ? (Refer to program above 10th Excercise in Practie notebook)
when someone asks you this question, you need to look at your solution and check,
what are your assumptions in the program?
did you cover both success and failure steps at each stage.

Before moving to the next section, Identify the gaps in above program which helps in calculating Somu bill and write your program below?

It should include all above concepts'''


product_list=['A','B','C']
product_list_cost=[10,20,30]
bill_amount = 0
#Below is a function defintion 
def apply_discount(amount,discount):
    #amount and discount are he parameters to the function
    final_amount = amount - (amount*discount)/100
    #final_amount is the return value from function, if there is nothing you can say return None
    return final_amount
def add_gst(final_bill_amount):
    gst_amount= final_bill_amount + (final_bill_amount*28)/100
    return gst_amount

for i in range(5):
    #To take input from users
    product_name  = input("Enter the product Name, A, B, C: ")
    if(product_name == 'NM'):
        break
    elif(product_name not in product_list):
        print("Wrong product name, Enter correct product name!")
        continue
    no_of_prods = input("Enter the number of products: ")
    if(product_name == product_list[0]):
        bill_amount += int(no_of_prods)*product_list_cost[0]
    elif(product_name == product_list[1]):
        bill_amount += int(no_of_prods)*product_list_cost[1]
    elif(product_name == product_list[2]):
        bill_amount += int(no_of_prods)*product_list_cost[2]
    

print("\nYour bill before discount - ",bill_amount)
#This is how the function call with arguments or parameters will work  
final_bill_amount = apply_discount(bill_amount,20)
if(final_bill_amount > 1000):
        bill_with_gst=add_gst(final_bill_amount)
        print("Your Final bill after discount with GST- ",bill_with_gst)
        print("you saved - ",bill_amount - final_bill_amount)
else:
    print("Your Final bill after discount - ",final_bill_amount)
    print("you saved - ",bill_amount - final_bill_amount)
