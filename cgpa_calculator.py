import csv
from tabulate import tabulate

def get_grade_points(grade):
    grade_points = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
    return grade_points.get(grade, "Invalid grade")

def cgpa_calculator(csv_file):
    """
    Calculate CGPA from a CSV file containing course details.
    """

    # Initialize variables to store course information and cumulative values
    courses = []
    total_unit = 0
    total_score = 0
    
    # Read course details from the CSV file
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader, None)
        for row in reader:
            if len(row) != 3:
                continue

            course_code = row[0]
            unit = int(row[1])
            grade = row[2].upper()
            grade_point = get_grade_points(grade)

            # Check if the grade is valid
            if grade_point == "Invalid grade":
                print(f"Invalid grade entered for course {course_code}.")
                continue

            # Calculate the total score for the course and add it to the courses list
            score = unit * grade_point
            courses.append([course_code, unit, grade_point, score])
            total_unit += unit
            total_score += score

    # Check if any courses were entered
    if not courses:
        return "No courses entered."

    # Create a table from the courses list
    headers = ["Course Code", "Course Unit", "Grade Point", "Total Grade Point"]
    table = tabulate(courses, headers=headers, tablefmt="fancy_grid", numalign="center")

    # Print the table
    print(table)

    # Print the total unit and total score
    print(f"Total unit: {total_unit}")
    print(f"Total score: {total_score}")

    # Print the total CGPA
    print(f"Total CGPA is: {total_score:.2f}/{total_unit:.2f}")
    
    # Calculate and return the CGPA if there are courses entered
    if total_unit > 0:
        cgpa = total_score / total_unit
        return f"Your CGPA is: {cgpa:.2f}"
    else:
        return "No courses entered."

# Assume the CSV file is named "courses.csv" and located in the same directory as the script
csv_file = "courses.csv"

# Call the cgpa_calculator() function with the CSV file path and store the result
result = cgpa_calculator(csv_file)

# Print the result
print(result)
