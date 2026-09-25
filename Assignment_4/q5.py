num = 153
original = num
sum = 0
while(num>0):
    i = num % 10
    num = num // 10
    sum += i**3
if(original== sum):
    print("Armstrong")