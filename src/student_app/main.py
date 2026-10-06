import json
import sys
from pathlib import Path

try:
    from utils.validate_name import validate_name
    from utils.validate_marks import validate_marks
    from Services.Calculator import calculate_grade
    from Report.student_report import display_report
    from config import APP_NAME, DEBUG, MAX_STUDENTS
    from logger import logger

except ImportError:
    project_root = Path(__file__).resolve().parents[2]

    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    sys.path.insert(0, str(Path(__file__).resolve().parent))

    from src.student_app.utils.validate_name import validate_name
    from src.student_app.utils.validate_marks import validate_marks
    from src.student_app.Services.Calculator import calculate_grade
    from src.student_app.Report.student_report import display_report
    from src.student_app.config import APP_NAME, DEBUG, MAX_STUDENTS
    from src.student_app.logger import logger


def main():
    logger.info("Application started")

    name = input("Enter student name: ")

    if not validate_name(name):
        print("Invalid name")
        logger.warning("Invalid student name entered")
        return

    try:
        marks = int(input("Enter marks: "))

        if not validate_marks(marks):
            print("Invalid marks")
            logger.warning("Invalid marks entered")
            return

    except ValueError:
        print("Invalid input. Marks must be a number.")
        logger.error("Invalid marks input: not a number")
        return

    grade = calculate_grade(marks)
    display_report(name, marks, grade)

    print(f"Application: {APP_NAME}")
    print(f"Debug mode: {DEBUG}")
    print(f"Maximum students: {MAX_STUDENTS}")

    project_root = Path(__file__).resolve().parents[2]
    json_path = project_root / "data" / "student.json"

    with open(json_path, "r") as file:
        student = json.load(file)

    print("\nStudent Information")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Program: {student['program']}")
    print(f"Semester: {student['semester']}")
    print(f"Marks: {student['marks']}")


if __name__ == "__main__":
    main()