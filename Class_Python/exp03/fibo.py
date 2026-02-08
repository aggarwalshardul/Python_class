n = int(input("Enter number: "))
a = 0
b = 1
sum = 0
for _ in range(n):
   
    sum = a+b
    a = b
    b = sum
    print(sum)

