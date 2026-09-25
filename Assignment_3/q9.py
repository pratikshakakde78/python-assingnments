S1 = int(input('Enter First subject marks:'))
S2 = int(input('Enter Second subject marks:'))
S3 = int(input('Enter Third subject marks:'))
S4 = int(input('Enter Fourth subject marks:'))
S5 = int(input('Enter Fifth subject marks:'))
per = ((S1 + S2 + S3 + S4 + S5 )/500)*100 

if(per>= 80 or per<= 100 ):
    print(' subject Grade is First class')
elif(per>=60 or per<= 80):
    print('subject Grade is Average class')
elif(per>=35 or per<= 60):
    print(' subject Grade is poor class')
else:
    print('Fail in this subject')

