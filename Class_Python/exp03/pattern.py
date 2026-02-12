n = 5

for i in range(n):
    
    for j in range(1, n - i + 1):
        print(j, end="")

    # spaces before stars
    print(" " * i, end="")

    # stars
    if i > 0:
        print("* " * i, end="")

    # right numbers
    for j in range(n - i, 0, -1):
        print(j, end="")

    print()
