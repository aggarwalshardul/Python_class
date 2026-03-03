# 8.	Write a program to check whether all the values in a dictionary are same or not using lambda function.

my_dict = {
    "a": 10,
    "b": 10,
    "c": 10
}

check = lambda d: len(set(d.values())) == 1

if check(my_dict):
    print("All values are same")
else:
    print("Values are not same")