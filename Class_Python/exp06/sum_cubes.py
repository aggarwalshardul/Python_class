# 2.	Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. 

def sum_cubes(n):
    sum=0
    i = 0
    while i<n:
        sum = sum + i*i*i
        i+=1
    return sum

n = int(input("Enter  the number: "))    

print("Sum of cubes: ",sum_cubes(n))