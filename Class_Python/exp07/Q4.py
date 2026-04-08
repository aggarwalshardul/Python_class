n = int(input("Enter number of test cases: "))

for i in range(n):
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)

    except ZeroDivisionError as e:
        print("Error Code:", e)

    except ValueError as e:
        print("Error Code:", e)