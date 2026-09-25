#Age1 = int(input('Enter age of people:'))
#Age2 = int(input('Enter age of people:'))
#Age3 = int(input('Enter age of people:'))
#Age4 = int(input('Enter age of people:'))
#Age5 = int(input('Enter age of people:'))
#t1 = int(input('Enter Ticket Amount:'))
Total = 0
for i in range(5):
    age = int(input("Enter Age:"))
    Amount = float(input('Enter Ticket Amount: '))
    
    if(age<12):
        A = Amount - (Amount*(30/100))
        print(f"Children Amount is {A}")
    elif(age >59):
        A = Amount - (Amount*(50/100))
        print(f"older people Ticket Amount is{A}")
    else:
        A = Amount
        print(f"No Discount {A}")
    Total += A
    print(f"Total Amount is {Total}")
    


