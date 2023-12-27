import tkinter as tk
import csv
import os
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image,ImageTk

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'registered.txt')

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

#font function
def init_fonts():
    return font.Font(family="Times New Roman", size=15)

#login page
def login_page(main):
    main.geometry("5000x5000")
    main.title("College Placement Program Login")
    custom_font = init_fonts()

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
                        msg_label.config(text="Wrong Password")
        if not condition:
            msg_label.config(text=f"{username} does not exist")

    title_label = tk.Label(main, text="Welcome to College Placement program! Please Login!", width=40, height=2,
                           font=custom_font,)
    title_label.pack(pady=70)
    make_text_bold(title_label)

    name_label = tk.Label(main, text="Username:", width=30, height=2, font=custom_font)
    name_label.pack()

    name_entry = tk.Entry(main, width=60, font=custom_font)
    name_entry.pack()

    password_label = tk.Label(main, text="Password:", width=30, height=2, font=custom_font)
    password_label.pack()

    password_entry = tk.Entry(main, width=60, show="*")
    password_entry.pack()

    login_button = tk.Button(main, text="Login", font=custom_font, command=command_on_login, height=2, width=15 ,fg="white",bg="green")
    login_button.pack(pady=30)

    signup_label = tk.Label(main, text="Haven't registered yet? Register now:", width=30, height=2, font=custom_font)
    signup_label.pack(pady=20)
    make_text_bold(signup_label)
    signup_button = tk.Button(main, text="Register", font=custom_font, command=command_on_signin, height=2, width=15,fg="white",bg="green")
    signup_button.pack()

    msg_label = tk.Label(main, height=2, width=40, font=custom_font, fg='red')
    msg_label.pack()

#signup page
def signin_page(main):
    main.geometry("5000x5000")
    main.title("Student College Placement Program Signup")
    custom_font = init_fonts()

    def command_on_signup():
        username = username_entry.get()
        password = password_entry.get()
        condition = False
        with open(file_path, 'r') as file:
            passpairs = csv.DictReader(file)
            for row in passpairs:
                if username == row['username']:
                    msg_label.config(text="Enter different username")
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

    email_label = tk.Label(main, text="Email:", height=2, width=40, font=custom_font)
    email_label.pack()

    email_entry = tk.Entry(main, width=60, font=custom_font)
    email_entry.pack()

    email_password_label = tk.Label(main, text="Email Password:", height=2, width=40, font=custom_font)
    email_password_label.pack()

    email_password_entry = tk.Entry(main, width=60, show='*')
    email_password_entry.pack()

    username_label = tk.Label(main, text="Username:", height=2, width=40, font=custom_font)
    username_label.pack()

    username_entry = tk.Entry(main, width=60, font=custom_font)
    username_entry.pack()

    password_label = tk.Label(main, text="Password:", height=2, width=40, font=custom_font)
    password_label.pack()

    password_entry = tk.Entry(main, width=60, show='*')
    password_entry.pack()

    signup_button = tk.Button(main, height=2, width=15, text="Signup", font=custom_font, command=command_on_signup,fg="white",bg="green")
    signup_button.pack(pady=30)

    msg_label = tk.Label(main, height=2, width=40, font=custom_font, fg='red')
    msg_label.pack()

#percentage function
def credentials_page(main):
    main.title("Student College Program Credentials")
    main.geometry("5000x5000")
    custom_font = init_fonts()

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
        else:
            messagebox.showerror("Error", "Please enter a valid percentage between 0 and 100.")
        if percentage > 50:
            discipline_choice()

#college page
    def show_colleges(selected_discipline):
        colleges_window = tk.Toplevel(main)
        colleges_window.geometry("600x600")
        colleges_window.title("List of Colleges")

        label_colleges = tk.Label(colleges_window, text=f"Colleges for {selected_discipline}:", font=custom_font)
        label_colleges.pack()
        
        college_list = []

        if selected_discipline == "Science":
            college_list = ["Science College A", "Science College B", "Science College C"]
        elif selected_discipline == "Commerce":
            college_list = ["Commerce College X", "Commerce College Y", "Commerce College Z"]
        elif selected_discipline == "Engineering":
            college_list = ["Engineering Institute 1", "Engineering Institute 2", "Engineering Institute 3"]
        elif selected_discipline == "Computer Science":
            college_list = ["CS Institute P", "CS Institute Q", "CS Institute R"]

        for college in college_list:
            tk.Label(colleges_window, text=college, font=custom_font).pack()

#discipline page
    def discipline_choice():
        discipline = tk.Toplevel(main)
        discipline.title("Discipline Selection")
        discipline.geometry("600x600")
        discipline_label = tk.Label(discipline, text="Select Discipline:", font=custom_font)
        discipline_label.grid(row=0, column=0, padx=10, pady=10)
        selected_discipline = tk.StringVar()
        discipline_option = tk.OptionMenu(discipline, selected_discipline, "Science", "Commerce", "Engineering",
                                           "Computer Science")
        discipline_option.grid(row=0, column=1, padx=10, pady=10)
        btn_show_colleges = tk.Button(discipline, text="Show Colleges", command=lambda: show_colleges(selected_discipline.get()),fg="white",bg="green")
        btn_show_colleges.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

#percentage page
    Name = tk.Label(main, text="Enter Your Name:",font=custom_font)
    Name.grid(row=0, column=0, padx=70, pady=10)

    Name_Entry = tk.Entry(main, fg='#42b3f5',font=custom_font)
    Name_Entry.grid(row=0, column=1, padx=70, pady=10)

    label_School = tk.Label(main, text="Enter Your School:",font=custom_font)
    label_School.grid(row=1, column=0, padx=70, pady=10)

    School_Entry = tk.Entry(main, fg='#42b3f5',font=custom_font)
    School_Entry.grid(row=1, column=1, padx=70, pady=10)

    label_District = tk.Label(main, text="Enter Your District:",font=custom_font)
    label_District.grid(row=2, column=0, padx=70, pady=10)

    District_Entry = tk.Entry(main, fg='#42b3f5',font=custom_font)
    District_Entry.grid(row=2, column=1, padx=70, pady=10)

    label_Percentage = tk.Label(main, text="Enter Percentage:",font=custom_font)
    label_Percentage.grid(row=3, column=0, padx=70, pady=10)

    percentage_Entry = tk.Entry(main,font=custom_font)
    percentage_Entry.grid(row=3, column=1, padx=70, pady=10)

    Grade_button = tk.Button(main, text="Calculate Grade", command=calculate_grade,font=custom_font,fg="white",bg="green")
    Grade_button.grid(row=4, column=0, columnspan=2, padx=70, pady=10)

    result_label = tk.Label(main, text="",font=custom_font)
    result_label.grid(row=5, column=0, columnspan=2, padx=70, pady=10)

main=tk.Tk()
login_page(main)
main.mainloop()