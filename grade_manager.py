import json

# --------------------------
# LOAD STUDENTS FROM FILE
# --------------------------
def load_students():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# --------------------------
# SAVE STUDENTS TO FILE
# --------------------------
def save_students(students):
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)

# --------------------------
# ADD STUDENT FUNCTION
# --------------------------
def add_student(name, grades):
    if not isinstance(grades, dict):
        raise ValueError("Grades must be a dictionary")
    students = load_students()
    student = {"name": name, "grades": grades}
    students.append(student)
    save_students(students)
    return student

# --------------------------
# VIEW STUDENTS FUNCTION
# --------------------------
def view_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    for idx, s in enumerate(students, start=1):
        print(f"{idx}. Name: {s['name']}, Grades: {s['grades']}")

# --------------------------
# CALCULATE GPA FUNCTION
# --------------------------
def calculate_score(grades):
    if not grades:
        return 0
    total = sum(grades.values())
    return total / len(grades)

# --------------------------
# MAIN MENU
# --------------------------
if __name__ == "__main__":
    while True:
        print("\n===== Student Score Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        try:
            choice = int(input("Enter choice (1-3): "))
            if choice == 1:
                name = input("Enter name: ")
                grades = {}

                while True:
                    subject = input("Enter subject (or type 'done' to finish): ")
                    if subject.lower() == 'done':
                        break
                    try:
                        score = float(input(f"Enter score for {subject}: "))
                        grades[subject] = score
                    except ValueError:
                        print("Score must be a number.")

                if grades:
                    student = add_student(name, grades)
                    gpa = calculate_score(student["grades"])
                    print(f"Student added! GPA: {gpa:.2f}")
                else:
                    print("No grades entered. Student not added.")


            elif choice == 2:
                view_students()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Please enter a valid option (1-3).")
        except Exception as e:
            print(f"Error: {e}")
