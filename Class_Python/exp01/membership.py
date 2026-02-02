#14.Using membership operator find whether a given number is in sequence (10,20,56,78,89)
seq = (10, 20, 56, 78, 89)

num = int(input("Enter a number: "))

if num in seq:
    print("Number is present in the sequence")
else:
    print("Number is NOT present in the sequence")
