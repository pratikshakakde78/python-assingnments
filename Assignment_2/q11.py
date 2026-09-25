M = int(input("Enter money Amount:"))

num1 = M // 500
r1 = M % 500

num2 = r1 // 200
r2 = r1 % 200

num3 = r2 // 100
r3 = r2 % 100

num4 = r3 // 50
r4 = r3 % 50

num5 = r4 // 20
r5 = r4 % 20

num6 = r5 // 10
r6 = r5 % 10
print(f"no. of notes 500 is:{num1}")
print(f"no. of notes 200 is:{num2}")
print(f"no. of notes 100 is:{num3}")
print(f"no. of notes 50 is:{num4}")
print(f"no. of notes 20 is:{num5}")
print(f"no. of notes 10 is:{num6}")
print(f"remaining Amount is:{r6}")