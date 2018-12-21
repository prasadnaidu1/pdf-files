'''You are back from US and you have only dollars, so you need cash in Rupees, you went to money exchange center. the person there will ask you how many dollars ? he will convert it to ruppees, deduct conversion charge and tell you the amount you will get.
Write a function which will take money in dollars and return rupees (use 1 dollar = 65 Rs) Write another function which deducts 1% of the converted money value as conversion charge and give the result to customer'''



main_prog()
def main_prog():
    nu_dollers = int(input("Enter number of dollers:"))
    rupees=convert_to_rupees(nu_dollers)
    comission_amount = comission_cal(rupees)
    result = rupees - comission_amount
    print("Amount is:",result)
    print("comission amount:",comission_amount)
def convert_to_rupees(nu_usd):
    return nu_usd * 65
def comission_cal(rupee):
    return (rupee*1)/100