# 9.	Write a program to create two lists and generate a dictionary with keys from list1 and values from list2.

list1 = ["a", "b", "c"]
list2 = [10, 20, 30]
result = dict(zip(list1, list2))

print("Generated Dictionary:", result)