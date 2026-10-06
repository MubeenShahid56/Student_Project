def calculate_grade(marks):
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade

def get_grade_description(grade):
    descriptions = {
        "A": "Excellent",
        "B": "Good",
        "C": "Average",
        "D": "Pass",
        "F": "Fail"
    }

    return descriptions.get(grade, "Unknown")