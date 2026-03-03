# 4.	Write a recursive function to print Fibonacci series upto n terms.

def fibo(n,a=0,b=1):
    if n==0:
        return 0
    print(a)
    fibo(n-1,b,a+b)
    
    

n = int(input("Enter the number: "))
fibo(n)
    
