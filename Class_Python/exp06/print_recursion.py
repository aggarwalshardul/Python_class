# 3.	Write a Python function to print 1 to n using recursion. (Note: Do not use loop)

def num(n):
    if n==0:
        return 
    num(n-1)
    print(n)

n=int(input("Enter the number: "))
num(n)