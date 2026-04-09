# Program to calculate Mean, Median, and Mode
import statistics
scores = [88, 92, 76, 81, 95, 89, 77, 85, 91, 87]
mean_score = statistics.mean(scores)
median_score = statistics.median(scores)
try:
    mode_score = statistics.mode(scores)
except statistics.StatisticsError:
    mode_score = "No unique mode"
print("Scores:", scores)
print("Mean:", mean_score)
print("Median:", median_score)
print("Mode:", mode_score)