num1 = int(input("Enter three digit number is:"))

d1 = num1 % 10
print(d1)
num2 = num1//10

d2 = num2 % 10
print(d2)
num3 = num2 // 10

d3 = num3 % 10
print(d3)
sum = d1 + d2 + d3
print(f"The addition of three digit number is:{sum}")