'''Take the program you wrote in Try it #07
pass the product A and B prices as arguments and take the values from sys.argv
and rerun the program. 
AS you use files here, you need to learn how to run python from command line. 
If you are Anaconda Navigator --> Click on Environment --> Root Start button --> Open Terminal 
you can run python here 
or if you installed python directly and set it in environment variables, you can goto command prompt and run python '''


import sys
a_cost = int(sys.argv[1])
b_cost = int(sys.argv[2])
num_prod_a= int(input("How Many product A?:"))
num_prod_b= int(input("How many product B?:"))
amount = num_prod_a * a_cost + num_prod_b * b_cost
discount_amount = (amount*10)/100
bill_amount = amount - discount_amount
print("Your bill before discount:",amount)
print("Final Bill Amount:",bill_amount)
print("You saved amount:",discount_amount)
