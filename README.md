# CGPA Calculator

This Python script calculates the Cumulative Grade Point Average (CGPA) based on course details provided in a CSV file named "courses.csv" located in the same directory as the script. It uses the `csv` module to read the CSV file and the `tabulate` library to display the course details in a tabular format.

## Requirements
- Python 3.x
- `csv` module (comes pre-installed with Python)
- `tabulate` library (install using `pip install tabulate`)

## How to Use
1. Ensure you have Python 3.x installed on your system.
2. Install the required `tabulate` library by running `pip install tabulate` in your terminal or command prompt.
3. Create a CSV file named "courses.csv" with the following format:

   ```
   Course Code, Course Unit, Grade
   CSC101, 3, A
   MAT201, 4, B
   PHY301, 3, C
   ...
   ```

   Replace the sample course codes, units, and grades with your actual course details. The grade should be one of the following: "A", "B", "C", "D", or "F". If any other grade is entered, it will be treated as invalid.

4. Save the "courses.csv" file in the same directory as this script.

5. Run the script using the following command:

   ```
   python cgpa_calculator.py
   ```

   Replace `cgpa_calculator.py` with the actual name of the Python script.

6. The script will process the course details from the "courses.csv" file and display them in a tabular format. It will also calculate the total unit, total score, and CGPA. The result will be printed in the terminal or command prompt.

## Function Explanation

The script contains the following functions:

### `get_grade_points(grade)`
This function takes a single argument `grade`, which represents the letter grade obtained in a course. It returns the corresponding grade points for the grade, and if the grade is invalid, it returns the string "Invalid grade".

### `cgpa_calculator(csv_file)`
This is the main function that calculates the CGPA based on the course details provided in the CSV file. It takes the `csv_file` as an argument, which is the name of the CSV file containing course details.

The function does the following:
- Initializes variables to store course information and cumulative values.
- Reads course details from the CSV file.
- Calculates the total score and grade points for each course.
- Creates a table from the course details and displays it using the `tabulate` library.
- Calculates the total unit, total score, and CGPA.
- Returns the calculated CGPA as a formatted string.

Note: If no courses are entered in the CSV file or if all grades are invalid, the function will return an appropriate message.

## Example Output

The output of running the script will look like this:

```
╒═════════════╤═════════════╤═════════════╤═══════════════════╕
│ Course Code │ Course Unit │ Grade Point │ Total Grade Point │
╞═════════════╪═════════════╪═════════════╪═══════════════════╡
│ CSC101      │ 3           │ 4           │ 12                │
├─────────────┼─────────────┼─────────────┼───────────────────┤
│ MAT201      │ 4           │ 3           │ 12                │
├─────────────┼─────────────┼─────────────┼───────────────────┤
| PHY301      | 3           | 2           | 6                 |
├─────────────┼─────────────┼─────────────┼───────────────────┤
│ Total       │ 10          │             │ 30                │
╘═════════════╧═════════════╧═════════════╧═══════════════════╛
Total unit: 10
Total score: 30
Total CGPA is: 3.00/10.00
Your CGPA is: 3.00
```

The table displays the course code, course unit, grade point, and total grade point for each course. The total unit, total score, and CGPA are also shown.

If there are no courses entered or if all grades are invalid, the script will display an appropriate message.