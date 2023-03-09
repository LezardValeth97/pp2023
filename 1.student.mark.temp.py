# Ask the user to input a number of unit (course / student)
def input_something(args):
    return int(input(f"Enter the number of {args} in this class: "));

# Ask the user to enter a list of info for an type
def input_infos(args):
    item = {}

    # TODO: input info for the type (student/course info)

    return item

# Input the student mark in a course base on the course id
def input_mark():

    student["marks"] = {}
    # TODO: check mark in student or not
    # If not, enter the mark for the course


# Display a list of students
def list_students(students):

    # TODO: check what happens if there's no student (hint: len(students))
    print("There aren't any students yet")

    # TODO: display the student list
    print("Here is the student list: ")

    # TODO: add loop function to check the info of student
    print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}")

    # TODO: check if mark student and print out the information
    if "marks" in student:
        print("Marks (Course Id - Mark): ", end="")   

# Display a list of courses
def list_courses(courses):
    # TODO: check what happens if there's no course (hint: len(course))
    print("There aren't any courses yet")
        
    print("Here is the course list: ")
    # TODO: add loop function to check the info of course
    print(f"{i+1}. {course['id']} - {course['name']}")

# Main function for the "game"
def main():
    # Initialize the list for DATA option
    courses = []
    students = []
    num_students = 0
    num_courses = 0

    while(True):
        print("""
    0. Exit
    1. 
    2. 
    ...
    n
    """)
        option = int(input("Your choice: "))                                                         # Choose option from 0 -> n
        if option == 0:
            break

        elif option == 1:                                                                            # Option 1
            input_something(student)
        elif option == 2:                                                                            # Option 2                                                     
            input_infos(course)
        ... ... 

        elif option == n:                                                                            # Option n
            # last function (your choice)
        else:
            print("Invalid input. Please try again!")

# Call the main function
if __name__ == "__main__":
    main()