unit = float(input("Enter the unit:"))
if(unit > 1 and unit < 50):
    Total_Amount = unit * 0.50
    print(f'Total Amount if unit is less than 50 is: { Total_Amount}')
elif(unit > 50 and unit < 100 ):
    Total_Amount = unit * 0.75
    print(f'Total Amount is: { Total_Amount}')
elif(unit > 100 and unit < 250 ):
    Total_Amount = unit * 1.20
    print(f'Total Amount is: { Total_Amount}')
elif(unit > 250):
    Total_Amount = unit * 1.50
    print(f'Total Amount is: { Total_Amount}')
else:
    print("invalid number")