n = 28
original = n
sum = 0
for i in range(1,n):
    if(28 % i == 0):
        sum += i
if(sum == original):
    print(f"Perfect number {sum}")
else:
    print("not perfect")