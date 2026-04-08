#Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.
# Enter number of students
n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(n):
    print("\nEnter marks for student", i+1)

    total_marks = 0

    # Input marks of 5 subjects
    for j in range(5):
        marks = int(input(f"Subject {j+1}: "))
        total_marks += marks

    # Calculate percentage
    percentage = total_marks / 5
    print("Percentage =", percentage)

    total_percentage += percentage

# Calculate average percentage of all students
average = total_percentage / n
print("\nAverage Percentage of all students =", average)
