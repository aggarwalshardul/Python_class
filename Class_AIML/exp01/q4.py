import random
import statistics

students = [
    "Aarav","Aaryan","Aditya","Akash","Aman","Amit","Aniket","Animesh","Ankit","Anmol","Arjun","Aryan","Ayush","Bhavesh","Chirag",
    "Dev","Dhruv","Gaurav","Harsh","Ishaan","Karan","Kartik","Ketan","Kunal","Kush","Manish","Mohit","Naman","Nikhil","Pankaj",
    "Pranav","Rahul","Raj","Rajat","Ravi","Rohit","Rohan","Sachin","Sagar","Sahil","Sandeep","Sanjay","Shivam","Shubham","Siddharth",
    "Sumit","Suraj","Tanishq","Uday","Varun","Aanchal","Aditi","Alka","Anamika","Ananya","Anjali","Ankita","Aparna","Archana","Bhavya",
    "Deepika","Divya","Isha","Kajal","Kavya","Khushi","Komal","Megha","Neha","Nikita","Pooja","Priya","Radhika","Ritu","Riya","Sakshi",
    "Shalini","Shivani","Shruti","Sneha","Sonali","Suman","Swati","Tanvi","Trisha","Vaishali","Vandana","Yashika","Zoya","Kritika"
]

marks = [random.randint(0, 100) for _ in students]

student_marks = dict(zip(students, marks))

meanmarks = statistics.mean(marks)
medianmarks = statistics.median(marks)
modemarks = statistics.mode(marks)
variance = statistics.variance(marks)
stddevmarks = statistics.stdev(marks)

print("Original Statistical Data")
print("Mean:", meanmarks)
print("Median:", medianmarks)
print("Mode:", modemarks)
print("Variance:", variance)
print("Standard Deviation:", stddevmarks)
sorted_marks = sorted(marks)

quartiles = statistics.quantiles(sorted_marks, n=4)

q1 = quartiles[0]
q2 = statistics.median(sorted_marks)
q3 = quartiles[2]

iqr = q3 - q1

lowerlimit = q1 - 1.5 * iqr
upperlimit = q3 + 1.5 * iqr

print("\nQuartile Data")
print("Q1:", q1)
print("Q2 (Median):", q2)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Limit:", lowerlimit)
print("Upper Limit:", upperlimit)

filtered_students = {
    student: mark
    for student, mark in student_marks.items()
    if lowerlimit <= mark <= upperlimit
}

print("\nFiltered Students (After Removing Outliers):")
print(filtered_students)

filtered_marks = list(filtered_students.values())
if filtered_marks:
    mean_val = statistics.mean(filtered_marks)
    median_val = statistics.median(filtered_marks)
    mode_val = statistics.mode(filtered_marks)
    variance_val = statistics.variance(filtered_marks)
    std_dev_val = statistics.stdev(filtered_marks)

    print("\nAfter Filtration New Statistical Data")
    print("Mean:", mean_val)
    print("Median:", median_val)
    print("Mode:", mode_val)
    print("Variance:", variance_val)
    print("Standard Deviation:", std_dev_val)
else:
    print("\nNo data left after filtering.")
