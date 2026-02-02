#13.	Write a program to find left shift and right shift values of a given number.
n = int(input("Enter a number: "))

left_shift = n << 1
right_shift = n >> 1

print("Left Shift (n << 1):", left_shift)
print("Right Shift (n >> 1):", right_shift)