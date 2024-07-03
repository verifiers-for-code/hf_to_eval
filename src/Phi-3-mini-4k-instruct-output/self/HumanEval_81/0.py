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
    1. Iterate over the list of numerical grades (GPAs):
        a. For each GPA in the list:
    
    2. Use if-elif-else conditionals to match each GPA with its corresponding letter grade, based on the provided grading table:
        a. If GPA > 4.0, output 'A+'
        b. Else if GPA > 3.7, output 'A'
        c. Continue with each grade level up to 'D-' and 'E'
    
    3. Handle edge cases, specifically:
        a. Return 'E' for a GPA of 0
        b. Make sure all GPA values are valid and non-negative
    
    4. Return a new list that contains the letter grades corresponding to each GPA
    
    5. Consider input validation and error handling as secondary steps if necessary, although these may be less critical based on the given information"""

    letter_grades = []
    for gpa in grades:
        if gpa > 4.0:
            letter_grades.append('A+')
        elif gpa > 3.7:
            letter_grades.append('A')
        elif gpa > 3.3:
            letter_grades.append('A-')
        elif gpa > 3.0:
            letter_grades.append('B+')
        elif gpa > 2.7:
            letter_grades.append('B')
        elif gpa > 2.3:
            letter_grades.append('B-')
        elif gpa > 2.0:
            letter_grades.append('C+')
        elif gpa > 1.7:
            letter_grades.append('C')
        elif gpa > 1.3:
            letter_grades.append('C-')
        elif gpa > 1.0:
            letter_grades.append('D+')
        elif gpa > 0.7:
            letter_grades.append('D')
        elif gpa > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades