class EmptyFileError(Exception):
    pass

class InvalidDataError(Exception):
    pass

try:
    with open("numbers.txt", "r") as f:
        data = f.read().strip()

        if not data:
            raise EmptyFileError("File is empty")

        nums = data.split()

        for n in nums:
            if not n.isdigit():
                raise InvalidDataError("Invalid data found")

        print("Valid file data")

except EmptyFileError as e:
    print(e)

except InvalidDataError as e:
    print(e)

except FileNotFoundError:
    print("File not found")