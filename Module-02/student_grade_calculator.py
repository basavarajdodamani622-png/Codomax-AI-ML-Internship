print("Student Grade Calculator")

name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Results ---")
print("Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 35:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
