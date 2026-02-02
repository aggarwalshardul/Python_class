#4.	Find the greatest among three numbers assuming no two values are same. 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a>b and a>c:
    print(a," is the greatest number")
elif b>c:
    print(b,"is the greatest number")
else:
    print(c," is the greatest number")
    