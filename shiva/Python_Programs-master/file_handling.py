''' File handling<br>

Function 1:
Somu want to create a file with all his bills so far, so take input from him until he says Done, and write it to a file, Bill no\tDate(DD/MM/YYYY)\tBill_amount

Function 2:
Now Somu wants to know what is his total expense out of bills. 
(optional) see if you can generate sub totals for each month. '''
file_access = open('bill1.txt','w+')
file_access.write("Bill No  Bill Date   Bill Amount"+'\n')
amount = 0
while(True):
    print("Menu\n1.Create a bill\n2.Total Expance\n3.Exit")
    choice = int(input("Enter your choice:"))
    if(choice == 1):
        while(True):
            user_input = input("Enter your choice(Say 'Bye' to exit  's' to continue):")
            if(user_input == 's'):
                data = ''
                bill_nu = input("Enter Bill number:")
                bill_date = input("Enter Bill Date:")
                bill_amount = input("Enter Bill Amount:")
                data = bill_nu+'\t'+bill_date+'\t'+bill_amount
                file_access.write(data+'\n')
            else:
                break
        print("Successfully saved")
        file_access.close()
        file_access_read = open('bill1.txt','r+')
        file_data = file_access_read.read()
        print(file_data)
    elif(choice == 2):
        file_access_read = open('bill1.txt','r+')
        file_data = file_access_read.read()
        #print(file_data)
        if(len(file_data) == 0):
            print("Empty Bill")
            file_access_read.close()
        else:
            bill_list = file_data.split('\n')
            #print(bill_list)
            for i in range(1,len(bill_list)-1):
                bill_list_lines = bill_list[i].split('\t')
                #print(bill_list_lines[2])
                amount = amount + int(bill_list_lines[2])
            print("Total Expances is:",amount)
            file_access_read.close()
    elif(choice == 3):
        print("Your are choosing Exit")
        break
        
    else:
        print("Invalid choice. Choose right choice")