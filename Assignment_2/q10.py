num1 = int(input("Enter three digit number is:"))

d1 = num1 % 10
mul1 = d1 * 100
num2 = num1//10

d2 = num2 % 10
mul2 = d2 * 10
num3 = num2 // 10

d3 = num3 % 10
mul3 = d3 * 1
sum = mul1 + mul2 + mul3
print(f"The reverse order of three digit number is:{sum}")