a = int(input("Enter first number a:"))
b = int(input("Enter second number b:"))
c = int(input("Enter third number c:"))

d = (b**2 - 4*a*c)**0.5
R1 = (-b + d) / 2 * a
R2 = (-b - d) / 2 * a
print(f"The first root R1 is:{R1}")
print(f"The second root R2 is:{R2}")
