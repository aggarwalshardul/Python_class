# 1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)

def min_max (seq):
    maximum = seq[0]
    minimum = seq[0]
    for x in seq[1: ]:
        if x > maximum:
         maximum= x
        if x < minimum:
            minimum = x
    return maximum,minimum

seq = [2,1,3,4,65,5]

min,Max = min_max(seq)

print("Maximum: ",min)
print("Minimum: ",Max)