A1 = int(input('Enter first Angle:'))
A2 = int(input('Enter second Angle:'))
A3 = int(input('Enter Third Angle:'))
angle = A1 + A2 + A3
if(angle == 180):
    print('Valid Triangle')
else:
    print('triangle is not valid')