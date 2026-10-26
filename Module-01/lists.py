# Module 01: Python Lists

subjects = ["Artificial Intelligence", "Machine Learning", "Python"]

print("Subjects:")
for subject in subjects:
    print(subject)

# Add a new subject
subjects.append("Deep Learning")

print("\nUpdated subjects:", subjects)

# Number of subjects
print("Total subjects:", len(subjects))
