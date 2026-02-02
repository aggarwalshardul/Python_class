#7.	Write a program which takes any date as input and display next date of the calendar
day = int(input("Enter Day:"))
month = int(input("Enter Month: "))
year = int(input("Enter Year: "))

if year%400==0 or year%4==0 and year%100!=0:
    leap = True
else:
    leap = False

if month in [1,3,5,7,8,10,12]:
    max_days = 31
if month == 2:
    if leap == True:
        max_days = 28
    else:
        max_days = 29
if month in [4,6,9,11]:
    max_days = 30
else:
    print("Invalid Entry")
max_month = 12
day+=1
if day>max_days:
    day = 1
    month +=1
if month > max_month:
    month = 1
    year+=1

print(f"Date: {day} - {month} - {year}")
