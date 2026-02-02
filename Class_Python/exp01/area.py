#8.	Write a program to find area of triangle when length of sides are given.
S1 = int(input("Enter side 1:"))
S2 = int(input("Enter side 2:"))
S3 = int(input("Enter side 3:"))

S = (S1+S2+S3)/2
Area = (S*(S-S1)*(S-S2)*(S-S3))**0.5
print("Area of Triangle = ",Area)
