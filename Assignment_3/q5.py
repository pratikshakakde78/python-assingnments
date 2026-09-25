S1 = input("Enter first side:")
S2 = input("Enter second side:")
S3 = input("Enter Third side:")
if(S1 + S2>S3 or S2 + S3> S1 or S1 + S3>S2):
    print("Valid Triangle")
    if(S1 == S2 == S3):
        print("Equilateral triangle")
    elif(S1 == S2 or S2==S3 or S1== S3):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Triangle is not valid")

