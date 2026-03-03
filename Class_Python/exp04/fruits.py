n = int(input("Enter number of fruits in each set: "))

s1 = set()
s2 = set()

print("\nEnter fruits for Set 1:")
for i in range(n):
    fruit = input()
    s1.add(fruit)

print("\nEnter fruits for Set 2:")
for i in range(n):
    fruit = input()
    s2.add(fruit)
common_fruits = s1 & s2
only_s1 = s1 - s2
total_fruits = len(s1 | s2)

print("\nFruits in both sets:", common_fruits)
print("Fruits only in Set 1:", only_s1)
print("Total count of unique fruits from both sets:", total_fruits)