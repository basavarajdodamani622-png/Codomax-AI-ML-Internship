
print("Student Grade Calculator")

name = input("Enter student name: ")

marks = []

for i in range(1, 4):
    while True:
        try:
            mark = float(input(f"Enter marks for Subject {i} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid marks! Enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

total = sum(marks)
average = total / len(marks)

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

print("\n--- Student Results ---")
print("Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
