# 4.	WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
str1 = input("Enter string: ")
str2=input("Enter substring:")
count=0
start=0
while True:
    pos = str1.find(str2, start)  
    
    if pos == -1:  
        break
    
    count += 1
    start = pos + 1   

print("Occurrences:", count)





