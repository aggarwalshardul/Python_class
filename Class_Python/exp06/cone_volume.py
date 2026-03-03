# 5.	Write a lambda function to find volume of cone.

v=lambda r,h: (1/3)*3.14*r*r*h
r = int(input("Enter radius: "))
h = int(input("Enter height: "))
print("Volume: ",v(r,h))