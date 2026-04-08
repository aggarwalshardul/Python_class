try:
    with open("city.txt", "r") as f:
        cities = [line.strip().split() for line in f]

    # a. Display all cities
    print("City Details:")
    for city in cities:
        print(city)

    # b. Population > 10 lakhs
    print("\nCities with population > 10 lakhs:")
    for city in cities:
        if float(city[1]) > 10:
            print(city[0])

    # c. Sum of areas
    total_area = sum(float(city[2]) for city in cities)
    print("\nTotal Area:", total_area)

except Exception as e:
    print("Error:", e)