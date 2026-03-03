s = input("Enter the string: ")
dict={}

for i in s:
    if i.isalpha():
        cap=i.upper()
        dict[cap]=dict.get(cap,0) + 1
for key in dict.keys():
    print(f"{dict[key]}{key}")