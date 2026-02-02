#8.	Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
pds = int(input("Marks in PDS: "))
python = int(input("Marks in Python: "))
chem = int(input("Marks in Chemistry: "))
phys = int(input("Marks in Physics: "))
eng = int(input("Marks in English: "))

percent = (pds+python+chem+phys+eng)/5
cgpa = (percent/10)

if cgpa >0 and cgpa<3.5:
    grade = "F"
if cgpa >=3.5 and cgpa<=5:
    grade = "C+"
if cgpa >5 and cgpa<=6:
    grade = "B"
if cgpa >6 and cgpa<=7:
    grade = "B+"
if cgpa >7 and cgpa<=8:
    grade = "A"
if cgpa >8 and cgpa<=9: 
    grade = "A+"
if cgpa >9 and cgpa<=10:
    grade = "O"

print("====GRADESHEET====")
print("Percentage: ",percent)
print("CGPA: ",cgpa)
print("Grade",grade)
