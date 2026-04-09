# Program to calculate Variance and Standard Deviation
import statistics
scores = [88, 92, 76, 81, 95, 89, 77, 85, 91, 87]
variance_score = statistics.variance(scores)
std_dev_score = statistics.stdev(scores)
print("Scores:", scores)
print("Variance:", variance_score)
print("Standard Deviation:", std_dev_score)