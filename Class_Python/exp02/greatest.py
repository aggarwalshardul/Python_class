#3.	Find the greatest among the two numbers. If numbers are equal than print “numbers are equal”. 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a>b:
    print(a," is greater then ",b)
elif b>a:
    print(b," is greater then ",a)
else:
    print("Number are equal")