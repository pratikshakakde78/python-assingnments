CP = int(input("Enter Cost Prise:"))
SP = int(input("Enter Selling Price:"))
Amount = SP - CP 
if(Amount>0):
    print("Got Profit Amount is {Amount}")
elif(Amount == 0):
    print("Neutral")
else:
    print("Got Loss Amount is {Amount}")