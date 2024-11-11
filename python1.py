# This program takes students' names and marks, stores them, and gives the average marks of a specified student

print("Enter the number of students you want to enter:")
n = int(input())

# Empty dictionary to store names and their list of marks as key-value pairs
Student_marks = {}

for _ in range(n):
    name, *line = input("Enter the name and marks of {} students separated by space: ".format(n)).split()
    
    # Convert each score in 'line' to a float and store it in the dictionary
    try:
        scores = list(map(float, line))  # Converts marks to a list of floats
        Student_marks[name] = scores
    except ValueError:
        print(f"Invalid input for {name}. Please enter numeric values for marks.")
        continue  # Skip to the next iteration if there's an error in conversion

query_name = input("Enter the name of the student to query: ")

# Calculate and print the average if the student exists in the dictionary
if query_name in Student_marks:
    Avg_Score = sum(Student_marks[query_name]) / len(Student_marks[query_name])
    print(f"Average score of {query_name} is: {Avg_Score:.2f}")
else:
    print("Student not found. Please check the name and try again.")




