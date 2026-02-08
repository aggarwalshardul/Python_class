# 4.	Write a program to find if given number is prime number or not.
n = int(input("Enter number: "))

for i in range (1,n):
    if(n%i==0):
        p =1
    else:
        p = 0

