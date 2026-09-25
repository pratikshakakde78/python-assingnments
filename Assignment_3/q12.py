num = int(input('Enter three Digit number:'))
r1 = num % 10 # 1
mul1 = r1 *100
num1 = num // 10 
r2 = num1 % 10 #2
mul2 = r2 * 10
num2= num1 // 10 #3
r3 = num2 % 10
mul3 = r3 * 1
sum = mul1 + mul2 + mul3
if(num == sum):
    print("number is Palindrome")
else:
    print(' number is not palindrome')

