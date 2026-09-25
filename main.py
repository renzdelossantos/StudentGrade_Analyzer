def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def letter_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def get_valid_number(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
            print(f"Please enter a number greater than or equal to {minimum}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid score. Please enter a numeric value.")


def add_student():
    name = input("Enter student name: ").strip()
    while not name:
        print("Student name cannot be empty.")
        name = input("Enter student name: ").strip()

    number_of_subjects = get_valid_number("How many subjects does this student have? ", 1)
    scores = []

    for subject_number in range(1, number_of_subjects + 1):
        score = get_valid_score(f"Enter score for subject {subject_number}: ")
        scores.append(score)

    average = calculate_average(scores)
    return {
        "name": name,
        "scores": scores,
        "average": average,
        "letter": letter_grade(average),
    }


def show_student_report(student):
    print(f"\nStudent: {student['name']}")
    print(f"Scores: {student['scores']}")
    print(f"Average: {student['average']:.2f}%")
    print(f"Letter Grade: {student['letter']}")


def show_class_summary(students):
    if not students:
        print("\nNo student data available.")
        return

    class_averages = [student["average"] for student in students]
    highest_average = max(class_averages)
    lowest_average = min(class_averages)
    overall_average = calculate_average(class_averages)
    passing_students = sum(1 for student in students if student["average"] >= 60)

    print("\n=== Class Summary ===")
    print(f"Total students: {len(students)}")
    print(f"Class average: {overall_average:.2f}%")
    print(f"Highest average: {highest_average:.2f}%")
    print(f"Lowest average: {lowest_average:.2f}%")
    print(f"Passing students: {passing_students}")
    print(f"Pass rate: {(passing_students / len(students)) * 100:.2f}%")


def main():
    print("====================================")
    print("      Student Grade Analyzer")
    print("====================================")

    students = []
    number_of_students = get_valid_number("How many students would you like to analyze? ", 1)

    for index in range(1, number_of_students + 1):
        print(f"\nEnter details for student {index}:")
        student = add_student()
        students.append(student)

    print("\n=== Student Results ===")
    for student in students:
        show_student_report(student)

    show_class_summary(students)

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()