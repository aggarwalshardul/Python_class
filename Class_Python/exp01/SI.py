#7.	Write a program to find simple interest.
p = int(input("Enter Total Amount: "))
r = int(input("Enter Rate of Interest:"))
t = int(input("Enter Time(in years): "))

SI = (p*r*t)/100
print("Simple Interest = ",SI)
