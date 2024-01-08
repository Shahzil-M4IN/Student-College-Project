import tkinter as tk
import csv
import os
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk



script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'registered.txt')
image_path = os.path.join(script_dir, "pexels-pixabay-159490.jpg")


###bold function
def make_text_bold(widget):
    custom_font = font.Font(widget, widget.cget("font"))  
    custom_font.configure(weight="bold") 
    widget.configure(font=custom_font) 


def switch_page(main, page):
    if main.winfo_exists():
        for widget in main.winfo_children():
            widget.destroy()
        switch_main = page(main)
    else:
        new_main = tk.Tk()
        switch_main = page(new_main)
    return switch_main

def init_fonts():
    return font.Font(family="Times New Roman", size=15)

#login page



def login_page(main):
    main.geometry("700x700")
    main.title("College Placement Program Login")
    custom_font = init_fonts()

    main.iconbitmap('Oxygen-Icons.org-Oxygen-Categories-applications-education-university.ico')

    background_image = ImageTk.PhotoImage(file=image_path)


    background_label = tk.Label(main, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image 

    def command_on_signin():
        switch_page(main, signin_page) 

    def command_on_login():
        username = name_entry.get()
        password = password_entry.get()
        condition = False
        with open(file_path, "r") as file:
            passpairs = csv.DictReader(file)
            for row in passpairs:
                if username == row["username"]:
                    condition = True
                    if password == row["password"]:
                        switch_page(main, credentials_page)
                        break
                    elif password != row["password"]:
                        msg_label.config(text="Wrong Password",font=custom_font, fg='red')
        if not condition:
            msg_label.config(text=f"{username} does not exist",font=custom_font, fg='red')

    title_label = tk.Label(main, text="Welcome to College Placement program! Please Login!", width=40, height=2,font=custom_font,)
    title_label.pack(pady=70)
    make_text_bold(title_label)

    name_label = tk.Label(main, text="Username:",font=custom_font)
    name_label.pack()

    name_entry = tk.Entry(main, width=30, font=custom_font)
    name_entry.pack(pady=10)

    password_label = tk.Label(main, text="Password:", font=custom_font)
    password_label.pack()

    password_entry = tk.Entry(main, width=30, show="*", font=custom_font)
    password_entry.pack(pady=10)

    login_button = tk.Button(main, text="Login", font=custom_font, command=command_on_login, height=2, width=15 ,fg="white",bg="green")
    login_button.pack(pady=30)

    signup_label = tk.Label(main, text="Haven't registered yet? Register now:", width=30, height=2, font=custom_font)
    signup_label.pack(pady=20)
    make_text_bold(signup_label)
    signup_button = tk.Button(main, text="Register", font=custom_font, command=command_on_signin, height=2, width=15,fg="white",bg="green")
    signup_button.pack()

    msg_label = tk.Label(main)
    msg_label.pack(pady=30)


#signup page
def signin_page(main):
    main.geometry("700x700")
    main.title("Student College Placement Program Signup")
    custom_font = init_fonts()

    main.iconbitmap('Oxygen-Icons.org-Oxygen-Categories-applications-education-university.ico')

    background_image = ImageTk.PhotoImage(file=image_path)


    background_label = tk.Label(main, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image 



    def command_on_signup():
        username = username_entry.get()
        password = password_entry.get()
        condition = False
        with open(file_path, 'r') as file:
            passpairs = csv.DictReader(file)
            for row in passpairs:
                if username == row['username']:
                    msg_label.config(text=f"{username} already exists",font=custom_font,fg='red')
                    break
            else:
                condition = True
        if condition:
            with open(file_path, 'a+') as file:
                file.write(f"\n{username},{password}")
            switch_page(main, login_page)

    title_label = tk.Label(main, text="Registration for Student College Program", height=2, width=40, font=custom_font)
    title_label.pack(pady=70)
    make_text_bold(title_label)

    email_label = tk.Label(main, text="Email:", font=custom_font)
    email_label.pack()

    email_entry = tk.Entry(main, width=30, font=custom_font)
    email_entry.pack(pady=10)

    email_password_label = tk.Label(main, text="Email Password:",font=custom_font)
    email_password_label.pack()

    email_password_entry = tk.Entry(main, width=30, show='*', font=custom_font)
    email_password_entry.pack(pady=10)

    username_label = tk.Label(main, text="Username:",font=custom_font)
    username_label.pack()

    username_entry = tk.Entry(main, width=30, font=custom_font)
    username_entry.pack(pady=10)

    password_label = tk.Label(main, text="Password:",font=custom_font)
    password_label.pack()

    password_entry = tk.Entry(main, width=30, show='*', font=custom_font)
    password_entry.pack(pady=10)

    signup_button = tk.Button(main, height=2, width=15, text="Signup", font=custom_font, command=command_on_signup,fg="white",bg="green")
    signup_button.pack(pady=30)

    msg_label = tk.Label(main)
    msg_label.pack()

#percentage function
def credentials_page(main):
    main.title("Student College Program Credentials")
    main.geometry("700x700")
    custom_font = init_fonts()

    background_image = ImageTk.PhotoImage(file=image_path)


    background_label = tk.Label(main, image=background_image)
    background_label.place(relwidth=1, relheight=1)
    background_label.image = background_image 

    def calculate_grade():
        percentage = float(percentage_Entry.get())
        if 0 <= percentage <= 100:
            if percentage >= 80:
                grade = 'A+'
            elif percentage >= 70:
                grade = 'A'
            elif percentage >= 60:
                grade = 'B'
            elif percentage >= 50:
                grade = 'C'
            else:
                grade = 'F'
            result_label.config(text=f"Grade: {grade}")
            discipline_choice()
            #show_colleges(matric_discip_entry.get(), float(percentage_Entry.get()))
        else:
            messagebox.showerror("Error", "Please enter a valid percentage between 0 and 100.")



#college page
    def show_colleges(selected_discipline, percentage):
        colleges_window = tk.Toplevel(main)
        colleges_window.geometry("600x600")
        colleges_window.title("List of Colleges")
        colleges_window.iconbitmap('Oxygen-Icons.org-Oxygen-Categories-applications-education-university.ico')
        label_colleges = tk.Label(colleges_window, text=f"Colleges for {selected_discipline}:", font=custom_font)
        label_colleges.pack()
        college_list = []

        if selected_discipline == "Pre-Medical":
            if 50 <= percentage < 60:
                college_list = [ "Jauhar Degree College"]
            if 60 <= percentage < 70:
                college_list = ["Govt. College For Men Nazimabad", "Jauhar Degree College"]
            if 70 <= percentage < 80:
                college_list = ["DJ Sindh Govt. Science College","Government Degree College Gulshan-e-Iqbal Block 7","Govt. College For Men Nazimabad", "Jauhar Degree College"]                
            elif 80 <= percentage <= 90:
                college_list = ["Adamjee Govt. Science College","DJ Sindh Govt. Science College","Government Degree College Gulshan-e-Iqbal Block 7", "Govt. College For Men Nazimabad", "Jauhar Degree College"]
        elif selected_discipline == "Commerce":
            if 50 <= percentage < 60:
                college_list = ["Jauhar Degree College"]
            if 60 <= percentage < 70:                
                college_list = ["Govt. College For Men Nazimabad", "Jauhar Degree College"]
            if 70 <= percentage < 80:
                college_list = ["DJ Sindh Govt. Science College","Government Degree College Gulshan-e-Iqbal Block 7","Govt. College For Men Nazimabad", "Jauhar Degree College"]    
            elif 80 <= percentage <= 90:
                college_list = ["Adamjee Govt. Science College","DJ Sindh Govt. Science College","Government Degree College Gulshan-e-Iqbal Block 7", "Govt. College For Men Nazimabad", "Jauhar Degree College"]
        elif selected_discipline == "Engineering":
            if 50 <= percentage < 60:
                college_list = ["Jauhar Degree College"]            
            if 60 <= percentage < 70:
                college_list = ["Govt. College For Men Nazimabad", "Jauhar Degree College"]
            if 70 <= percentage < 80:
                college_list = ["DJ Sindh Govt. Science College","Government Degree College Gulshan-e-Iqbal Block 7","Govt. College For Men Nazimabad", "Jauhar Degree College"]  
            elif 80 <= percentage <= 90:
                college_list = ["Adamjee Govt. Science College","DJ Sindh Govt. Science College","Government Degree College Gulshan-e-Iqbal Block 7", "Govt. College For Men Nazimabad", "Jauhar Degree College"]
        elif selected_discipline == "Computer Science":
            if 50 <= percentage < 60:
                college_list = ["Jauhar Degree College"]            
            if 60 <= percentage < 70:
                college_list = ["Govt. College For Men Nazimabad", "Jauhar Degree College"]
            if 70 <= percentage < 80:
                college_list = ["DJ Sindh Govt. Science College","Government Degree College Gulshan-e-Iqbal Block 7","Govt. College For Men Nazimabad", "Jauhar Degree College"]  
            elif 80 <= percentage <= 90:
                college_list = ["Adamjee Govt. Science College","DJ Sindh Govt. Science College","Government Degree College Gulshan-e-Iqbal Block 7", "Govt. College For Men Nazimabad", "Jauhar Degree College"]

        for college in college_list:
            tk.Label(colleges_window, text=college, font=custom_font).pack()

#discipline page
    def discipline_choice():
        discipline = tk.Toplevel(main)
        discipline.title("Discipline Selection")
        discipline.geometry("600x600")
        
        discipline.iconbitmap('Oxygen-Icons.org-Oxygen-Categories-applications-education-university.ico')

        background_image = ImageTk.PhotoImage(file=image_path)

        background_label = tk.Label(discipline, image=background_image)
        background_label.place(relwidth=1, relheight=1)
        background_label.image = background_image 

        discipline_label = tk.Label(discipline, text="Select Discipline:", font=custom_font)
        discipline_label.pack()
        selected_discipline = tk.StringVar()
        discipline_option = tk.OptionMenu(discipline, selected_discipline, "Pre-Medical", "Commerce", "Engineering",
                                           "Computer Science")
        discipline_option.pack()
        btn_show_colleges = tk.Button(discipline, text="Show Colleges", command=lambda: show_colleges(selected_discipline.get(),float(percentage_Entry.get())),fg="white",bg="green")
        btn_show_colleges.pack()
    
    def command_on_logout():
        switch_page(main,login_page)

    main.grid_columnconfigure(0, weight=1)
    main.grid_columnconfigure(1, weight=1)

#percentage page
    Name = tk.Label(main, text="Enter Your Name:",font=custom_font)
    Name.grid(row=0, column=0, padx=70, pady=10)

    Name_Entry = tk.Entry(main,font=custom_font)
    Name_Entry.grid(row=0, column=1, padx=70, pady=10)

    label_School = tk.Label(main, text="Enter Your School:",font=custom_font)
    label_School.grid(row=1, column=0, padx=70, pady=10)

    School_Entry = tk.Entry(main,font=custom_font)
    School_Entry.grid(row=1, column=1, padx=70, pady=10)

    label_District = tk.Label(main, text="Enter Your District:",font=custom_font)
    label_District.grid(row=2, column=0, padx=70, pady=10)

    District_Entry = tk.Entry(main,font=custom_font)
    District_Entry.grid(row=2, column=1, padx=70, pady=10)

    roll_no_label=tk.Label(main,font=custom_font,text="Enter Matric Roll No:")
    roll_no_label.grid(row=3,column=0,padx=70,pady=10)

    roll_no_entry=tk.Entry(main,font=custom_font)
    roll_no_entry.grid(row=3,column=1,padx=70,pady=10)

    matric_discip_label=tk.Label(main,font=custom_font,text="Discipline(Matric):")
    matric_discip_label.grid(row=4,column=0,padx=70,pady=10)

    matric_discip_entry=tk.Entry(main,font=custom_font)
    matric_discip_entry.grid(row=4,column=1,padx=70,pady=10)

    label_Percentage = tk.Label(main, text="Enter Percentage:",font=custom_font)
    label_Percentage.grid(row=5, column=0, padx=70, pady=10)

    percentage_Entry = tk.Entry(main,font=custom_font)
    percentage_Entry.grid(row=5, column=1, padx=70, pady=10)

    Grade_button = tk.Button(main, text="Calculate Grade", command=calculate_grade,font=custom_font,fg="white",bg="green")
    Grade_button.grid(row=6, column=0, columnspan=2, padx=70, pady=10)

    result_label = tk.Label(main, text="",font=custom_font)
    result_label.grid(row=7, column=0, columnspan=2, padx=70, pady=10)

    logout_button=tk.Button(main,text="Logout",command=command_on_logout,font=custom_font, height=2, width=15,fg="white",bg="green")
    logout_button.grid(row=12,column=0,columnspan=2,pady=150,padx=50)

main=tk.Tk()
login_page(main)
main.mainloop()