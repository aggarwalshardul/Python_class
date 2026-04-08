try:
    with open("numbers.txt", "r") as f:
        numbers = [int(line.strip()) for line in f]

    # a. Maximum number
    max_num = max(numbers)
    print("Maximum number:", max_num)

    # b. Average of numbers
    avg = sum(numbers) / len(numbers)
    print("Average:", avg)

    # c. Count numbers greater than 100
    count = sum(1 for n in numbers if n > 100)
    print("Numbers greater than 100:", count)

except FileNotFoundError:
    print("Error: File not found")

except ValueError:
    print("Error: File contains non-integer values")

except ZeroDivisionError:
    print("Error: File is empty")