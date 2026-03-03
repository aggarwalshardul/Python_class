# 2.	 Count total number of vowels in a given string.
s = input("Enter sting:")
s=s.lower()
count = 0
vowels=" aeiou"
for i in s:
    if i in vowels:
        count=count+1
print("Total Vowels: ",count)
