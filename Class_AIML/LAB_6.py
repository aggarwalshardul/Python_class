import random
import statistics


data = random.sample(range(1, 10000), 100)

#print(data)

min_val = min(data)
max_val = max(data)
data_range = max_val - min_val

normalized = []
if data_range == 0:
    print("Zero division error in Normalization")
else:
    for x in data:
        calc = (x - min_val) / data_range
        normalized.append(calc)

mean_data = statistics.mean(data)
standard_deviation = statistics.stdev(data)

standardization = []
if standard_deviation == 0:
    print("Zero division error in standardization")
else:
    for x in data:
        calc = (x - mean_data) / standard_deviation
        standardization.append(calc)

sorted_data = sorted(data)
n = len(sorted_data)
median = statistics.median(sorted_data)
q1 = sorted_data[n // 4]
q3 = sorted_data[(3 * n) // 4]
iqr = q3 - q1

robust_scaled = []
for x in data:
    calc = (x - median) / iqr if iqr != 0 else 0.0
    robust_scaled.append(calc)

max_abs = max(abs(x) for x in data)

max_abs_scaled = []
for x in data:
    calc = x / max_abs if max_abs != 0 else 0.0
    max_abs_scaled.append(calc)

print(f"\nOriginal (first 5): {data[:5]}")
print(f"\nNormalized (0 to 1): {normalized[:5]}")
print(f"\nStandardized (Mean 0): {standardization[:5]}")
print(f"\nRobust Scaled (Median 0): {robust_scaled[:5]}")
print(f"\nMax Absolute Scaled: {max_abs_scaled[:5]}")


