def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    

    Action Plan:
    1. Define a list of tuples, `grading_thresholds`, to represent the grading thresholds and corresponding letter grades.
    2. Create a function, `numerical_letter_grade`, that takes a list of GPAs as input.
    3. Initialize an empty list, `letter_grades`, to store the letter grades.
    4. Iterate through each GPA in the input list:
        a. Compare the GPA with the grading thresholds in `grading_thresholds`.
        b. If the GPA is greater than or equal to a threshold, assign the corresponding letter grade to `letter_grades`.
        c. If the GPA is less than a threshold, assign the corresponding letter grade to `letter_grades`.
    5. Return the list of letter grades, `letter_grades`.
    
    Note: Use a suitable data structure to store the grading thresholds and letter grades.
    Be careful when comparing GPAs with the grading thresholds."""
    
    grading_thresholds = [
        (4.0, 'A+'),
        (3.7, 'A'),
        (3.3, 'A-'),
        (3.0, 'B+'),
        (2.7, 'B'),
        (2.3, 'B-'),
        (2.0, 'C+'),
        (1.7, 'C'),
        (1.3, 'C-'),
        (1.0, 'D+'),
        (0.7, 'D'),
        (0.0, 'D-'),
        (0.0, 'E')
    ]
    
    letter_grades = []
    
    for gpa in grades:
        for threshold, letter_grade in grading_thresholds:
            if gpa >= threshold:
                letter_grades.append(letter_grade)
                break
        else:
            letter_grades.append('E')
    
    return letter_grades