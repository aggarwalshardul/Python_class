# 1.	 Write a program to count and display the number of capital letters in a given string.
n=input("Enter string: ")
count = 0

for i in n:
    if i>='A' and i<='Z':
        count = count+1
        print(i)
print(count)