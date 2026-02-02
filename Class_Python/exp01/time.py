#9.	Write a program to convert given seconds into hours, minutes and remaining seconds.
seconds = int(input("Enter total seconds: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", remaining_seconds)
