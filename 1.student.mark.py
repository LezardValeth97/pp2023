# Ask the user to input a number
def input_number(unit):
    return int(input(f"Enter the number of {unit} in this class: "));

# Ask the user to enter a list of info for an item_type
def input_infos(item_type, infos):
    item = {}
    for info in infos:
        item[info] = input(f"\tEnter the {item_type}'s {info}: ")
    return item

# Display a list of items
def display(lst):
    for i, item in enumerate(lst):
        print(f"{1+i}. {item}")

# Input the student mark in a course
def input_mark(student, course_id):
    if "marks" not in student:
        student["marks"] = {}
    student["marks"][course_id] = input("Enter the student's mark for this course: ")

# Display a list of students
def list_students(students):
    if len(students) <= 0:
        print("There aren't any students yet")
        return
    print("===> Here is the student list: ")
    for i, student in enumerate(students):
        print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}")
        if "marks" in student:
            print("Marks (Course Id - Mark): ", end="")
            for course_id, mark in student["marks"].items():
                print(f"({course_id} - {mark})", end="\t")
            print()

# Display a list of courses
def list_courses(courses):
    if len(courses) <= 0:
        print("There aren't any courses yet")
        return
    print("===> Here is the course list: ")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course['id']} - {course['name']}")

# Ask the user to enter an integer to select an option
def select(option_range, input_message="Choose an option: "):
    selection = input(input_message)
    if not selection.isnumeric():
        return -1
    selection = int(selection)
    if selection not in option_range:
        return -1
    return selection


# Pause the program
def pause():
    input("Press Enter to continue...")

# Main function
def main():
    courses = []
    students = []
    num_students = 0
    num_courses = 0
    while(True):
        print("""
===================================================
Here are the functions of this application
    0. Exit
    1. Input number of students
    2. Input students information (id, name, DoB)
    3. Input number of courses
    4. Input course information (id, name)
    5. Input marks for student in a course
    6. List courses
    7. List students""")       
        selection = select(range(0, 8))
        if selection == 0:
            break
        elif selection == 1:
            num_students = input_number("students")
            print(f"===> There are {num_students} student(s) in this class")
        elif selection == 2:
            if num_students <= 0:
                print("Please input the number of students first")
                pause()
                continue
            students = []
            for i in range(num_students):
                print(f"Student No. {i+1}")
                students.append(input_infos("student", ("id", "name", "DoB")))
            list_students(students)
        elif selection == 3:
            num_courses = input_number("courses")
            print(f"===> There are {num_courses} course(s) in this class")
        elif selection == 4:
            if num_courses <= 0:
                print("Please input the number of courses first")
                pause()
                continue
            courses = []
            for i in range(num_courses):
                print(f"Course No. {i+1}")
                courses.append(input_infos("course", ("id", "name")))
            list_courses(courses)
        elif selection == 5:
            list_courses(courses)
            if len(courses) > 0:
                selected_course = select(range(1, num_courses + 1), "Select a course: ") - 1
                if selected_course < 0:
                    print("Invalid input")
                else:
                    for i in range(num_students):
                        print(f"Student No. {i+1} - {students[i]['name']}. ",end="")
                        input_mark(students[i], courses[selected_course]["id"]) 
        elif selection == 6:
            list_courses(courses)
        elif selection == 7:
            list_students(students)
        else:
            print("Invalid input. Please try again!")
        pause() 

    #num_courses = input_number("courses")

if __name__ == "__main__":
    main()
