gender = input('Enter Gender(M/F):')
age = int(input("Enter age:"))

if(gender == 'M'):
    if(age >= 21):
        print("Boy Eligible for marriage")
    else:
        print('not Eligible')
else:
    if(age >= 18):
        print('Girl Eligible for marriage')
    else:
        print('Girl is not Eligible for marriage')