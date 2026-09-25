id = input("Enter userid :")
pass0 = input("Enter pass:")
id1 = input("Enter id to match first id:")
if(id == id1):
    print("userid is valid ")
    pass1 = input("Enter Password to match first pass:")
    if(pass0 == pass1):
        print("password is correct")
    else:
        print("incorrect password")
else:
    print("incorrect userid")
        
    