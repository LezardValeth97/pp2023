class Student:
    def __init__(self):
        self.__id = input("Enter the student's id: ")
        self.__name = input("Enter the student's name: ")
        self.__dob = input("Enter the student's dob: ")

    # Encapsulation part
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

class Course:
    def __init__(self):
        self.__id = input("Enter the course's id: ")
        self.__name = input("Enter the course's name: ")
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

class Utils:
    # Ask the user to input something
    def input_something(args):
        return int(input(f"Enter the number of {args}: "));

    # Show the list
    def show(list):
        for i in enumerate(list):
            # do something here

class University:
    def __init__(self):
        # Initialize the list for DATA option
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []

    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def set_num_students(self):
        std_numb = self.get_num_students()
        self.__num_students = Utils.input_something("students")            # Example of polyphomism

    def set_num_courses(self):
        crs_numb = self.get_num_courses()
        self.__num_courses = Utils.input_something("courses")              # Example of polyphomism

    def set_students(self):

    def set_courses(self):

    # Display a list of students
    def list_students(self):
        print("Student list: ")
        Utils.show(self.get_students())

    # Display a list of courses
    def list_courses(self):
        print("Course list: ")
        Utils.show(self.get_courses())

# Main function for the "game"
def main():
    univ = University()

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
            univ.set_students()
        elif option == 2:                                                                            # Option 2                                                     
            univ.set_courses()
        ... ... 

        elif option == n:                                                                            # Option n
            # last function (your choice)
            # univ.list_students() or univ.list_courses()
        else:
            print("Invalid input. Please try again!")


# Call the main function
if __name__ == "__main__":
    main()
