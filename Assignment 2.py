x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

if (x>y) and (x>z):
    print("x is the largest number")
elif (y>x) and (y>z):
    print("y is the largest number")
else:
    print("z is the largest number")
