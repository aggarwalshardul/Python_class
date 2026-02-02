#6.	Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem
l = int(input("Enter length: "))
b = int(input("Enter base: "))

c = (l*l + b*b)**0.5
print("Hypotenuse = ",c)
