import tkinter as tk

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student System Management")
        self.window.geometry("1540x700+0+0")

        # Frame in the left for all the buttons
        self.detail_frame = tk.Frame(
            self.window,
            bg="#4a536b", 
            relief=tk.GROOVE
        )
        self.detail_frame.place(width=260, height=700)

        # Buttons Frame for Display
        self.btn_frame_for_list = tk.Frame(
            self.detail_frame,
            bg='#4a536b', 
            relief=tk.GROOVE
        )
        self.btn_frame_for_list.place(x=50, y=40, width=310, height=130)


        #Display "Student" Button
        self.stdlist_btn = tk.Button(
            self.btn_frame_for_list,
            bg="#4a536b", 
            foreground="white",
            text="Student List",
            bd=2,
            font=("Times New Romans", 13), width=15,
            relief=tk.FLAT
        )
        self.stdlist_btn.grid(row=0, column=0, padx=2, pady=2)

        #Display "Course" Button
        self.crslist_btn = tk.Button(
            self.btn_frame_for_list,
            bg="#4a536b", 
            foreground="white",
            text="Course List",
            bd=2,
            font=("Times New Romans", 13), width=15,
            relief=tk.FLAT
        )
        self.crslist_btn.grid(row=1, column=0, padx=2, pady=2)


        #Buttons Frame for Adding
        self.btn_frame_for_input = tk.Frame(
            self.detail_frame,
            bg="#4a536b", 
            relief=tk.GROOVE
        )
        self.btn_frame_for_input.place(x=50, y=340, width=310, height=130)


        #Display "Student" Button
        self.add_btn = tk.Button(
            self.btn_frame_for_input,
            bg="#4a536b", 
            foreground="white",
            text="Input Info",
            bd=2,
            font=("Times New Romans", 13), width=15,
            relief=tk.RIDGE
            )
        self.add_btn.grid(row=0, column=0, padx=2, pady=2)

        #Frame in the right for the Data frame
        self.data_frame = tk.Frame(
            self.window,  
            relief=tk.GROOVE
        )
        self.data_frame.place(x=260, width=1280, height=700)


        #Top Menu 
        self.title_label = tk.Label(
            self.data_frame, 
            text="Student Management System",
            font=("Times New Romans", 15, "bold"),
            padx=400,
            pady=15, 
            border=0, 
            bg='#E0E0EE',
            relief=tk.GROOVE
        )
        self.title_label.pack(side=tk.TOP, fill=tk.X)

        self.info_frame = tk.Frame(
            self.data_frame,
            bg='#aed6dc',
            height=900,
            width=1300
        )
        self.info_frame.pack()

        # create a label in the info_frame to display the text
        self.display_label = tk.Label(
            self.info_frame,
            font=("Times New Romans", 20),
            bg='#aed6dc',
            justify=tk.CENTER,
            anchor=tk.CENTER,
            text=''
        )
        # self.display_label.pack(fill=tk.BOTH, expand=1)
        self.display_label.place(x=500, y=300)
        
        # configure stdlist_btn to display the student list
        self.stdlist_btn.config(command=self.display_student_list)
        
        # configure crslist_btn to display the course list
        self.crslist_btn.config(command=self.display_course_list)

        # create the input buttons for adding student and course info
        self.add_std_btn = tk.Button(
            self.info_frame,
            text="Input Student Info",
            font=("Times New Roman", 13),
            width=20,
            relief=tk.RAISED,
            command=self.show_student_input_frame  # add this line to set the command
        )

        self.add_crs_btn = tk.Button(
            self.info_frame,
            text="Input Course Info",
            font=("Times New Roman", 13),
            width=20,
            relief=tk.SUNKEN
        )

        self.add_mark_btn = tk.Button(
            self.info_frame,
            text="Input Mark",
            font=("Times New Roman", 13),
            width=20,
            relief=tk.GROOVE
        )

        # hide the input buttons initially
        self.add_std_btn.place_forget()
        self.add_crs_btn.place_forget()
        self.add_mark_btn.place_forget()

        # configure add_btn to display the input buttons
        self.add_btn.config(command=self.display_input_buttons)

    def display_input_buttons(self):
        # hide the student/course list labels if they are visible
        self.display_label.place_forget()

        # display the input buttons
        self.add_std_btn.place(x=400, y=300)
        self.add_crs_btn.place(x=600, y=300)
        self.add_mark_btn.place(x=800, y=300)

        # set the command of the add_std_btn to show the student input frame
        self.add_std_btn.config(command=self.show_student_input_frame)

    def display_student_list(self):
        # hide the input buttons if they are visible
        self.add_std_btn.place_forget()
        self.add_crs_btn.place_forget()
        self.add_mark_btn.place_forget()

        # display the student list label
        self.display_label.config(text="This is the student list")
        self.display_label.place(x=500, y=300)

    def display_course_list(self):
        # hide the input buttons if they are visible
        self.add_std_btn.place_forget()
        self.add_crs_btn.place_forget()
        self.add_mark_btn.place_forget()

        # display the course list label
        self.display_label.config(text="This is the course list")
        self.display_label.place(x=500, y=300)

    def show_student_input_frame(self):
        # hide the input buttons if they are visible
        self.add_std_btn.place_forget()
        self.add_crs_btn.place_forget()
        self.add_mark_btn.place_forget()

        # create a new frame for student input
        self.student_input_frame = tk.Frame(
            self.info_frame,
            height=900,
            width=1300,
            bg="white"
        )

        # display the student input frame
        self.student_input_frame.place(x=0, y=0)

        # create the widgets for the student input frame
        self.std_lab = tk.Label(
            self.student_input_frame, 
            text="Enter Student Info", 
            font=("Times New Roman", 16))
        self.std_lab.place(x=20, y=15)

        self.student_name_lab = tk.Label(
            self.student_input_frame, 
            text="Name: ",
            font=("Times New Roman", 16))
        self.student_name_lab.place(x=20, y=55)

        self.student_name_entry = tk.Entry(
            self.student_input_frame, 
            font=("Times New Roman", 13))
        self.student_name_entry.place(x=90, y=55, width=250, height=30)

        self.student_id_lab = tk.Label(
            self.student_input_frame,
            text="ID: ",
           font=("Times New Roman", 16))
        self.student_id_lab.place(x=20, y=95)

        self.student_id_entry = tk.Entry(
            self.student_input_frame, 
            font=("Times New Roman", 13))
        self.student_id_entry.place(x=90, y=95, width=250, height=30)

        # create a Back button
        self.back_button = tk.Button(
            self.student_input_frame,
            text="Back",
            font=("Times New Roman", 13),
            width=20,
            relief=tk.FLAT,
            command=self.show_info_frame  # this command will show the previous frame
        )
        self.back_button.place(x=650, y=450)

        # create a Submit button
        # ...

    def show_info_frame(self):
        # hide the current frame
        self.student_input_frame.place_forget()

        # show the previous frame
        self.info_frame.place()


# The main function
if __name__ == "__main__":
    root = tk.Tk()
    obj = Management(root)
    root.mainloop()