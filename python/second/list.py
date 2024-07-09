# List of subjects in the 4th semester
subjects_4th_semester = [
    "Mathematics IV",
    "Data Structures",
    "Database Management Systems",
    "Computer Organization",
    "Operating Systems",
    "Software Engineering",
    "Digital Logic Design"
]

# Display the list using a for loop
print("Subjects in the 4th semester:")
for subject in subjects_4th_semester:
    print(subject)

# Display 2nd and 5th elements of the list
print("\n2nd element:", subjects_4th_semester[1])
print("5th element:", subjects_4th_semester[4])

# Display first 4 elements of the list using the range of indexes
print("\nFirst 4 elements:", subjects_4th_semester[:4])

# Display last 4 elements of the list using the range of negative indexes
print("Last 4 elements:", subjects_4th_semester[-4:])

# Check if "Python Programming Lab" is available in the list
subject_to_check = "Python Programming Lab"
is_available = subject_to_check in subjects_4th_semester
print(f"\nIs '{subject_to_check}' available in the list?:", is_available)

# Demonstrate the working of append() function
subjects_4th_semester.append("Python Programming Lab")
print("\nAfter appending 'Python Programming Lab':", subjects_4th_semester)

# Demonstrate the working of insert() function
subjects_4th_semester.insert(3, "Machine Learning")
print("After inserting 'Machine Learning' at index 3:", subjects_4th_semester)

# Demonstrate the working of remove() function
subjects_4th_semester.remove("Software Engineering")
print("After removing 'Software Engineering':", subjects_4th_semester)

# Demonstrate the working of pop() function
popped_subject = subjects_4th_semester.pop(2)
print(f"After popping the subject at index 2: {popped_subject}")
print("Current list:", subjects_4th_semester)
