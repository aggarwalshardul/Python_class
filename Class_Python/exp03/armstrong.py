# 2.	Find whether the given number is Armstrong number.
n = int(input("Enter number: "))
pow = len(str(n))
temp = n
# for i in range (0,pow+1):
#     k = n%10
total = 0
while temp>0:
    r = temp%10
    total = total + r**pow
    temp = temp//10
if (total == n):
    print("Number is Armstrong number ")
else:
    print("Number is not Armstrong")



