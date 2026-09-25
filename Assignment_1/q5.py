P = int(input("Enter Principle Amount :"))
T = int(input("Enter Time:"))
R = int(input("Enter Rate(%):"))

CI = P * ((1 + R / 100 )**T) - P

print(f"The compound intrest is {CI}")