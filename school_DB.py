import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


db = mysql.connect(
    host="localhost",
    user="root",
    passwd="12344"
)

cursor = db.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS school")

cursor.execute("USE school")


# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS student(stu_id int primary key, fName varchar(30) not null, lName varchar(30) not null);")

# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS teachers(teacher_id int primary key, fName varchar(30) not null, lName varchar(30) not null);")

# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS subject(subject_id int primary key, title varchar(30) not null);")

# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS grade(grade_id int primary key, name varchar(30) not null);")


# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS marks(markid int primary key, mark int not null ,date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,student_id int,subject_id int );")

# cursor.execute("INSERT INTO student value(12347, 'yousra', 'mansour')")

# db.commit()
root = Tk()
root.iconbitmap("icon.ico")
root.title("SCHOOL")


def save_edit_stu():

    num_grade = grdes.index(var_ins_v.get()) + 1

    cursor.execute(
        f"UPDATE student SET stu_id = {int(stu_id_v.get())},fName='{fname_v.get()}', lName='{lname_v.get()}', grade_id = {num_grade}  WHERE stu_id = {old_id}")

    stu_id_entry.delete(0, END)
    stu_id_v.delete(0, END)
    fname_v.delete(0, END)
    lname_v.delete(0, END)
    var_ins_v.set("first grade")

    db.commit()


def View_info(student_id):
    cursor.execute(f" SELECT * FROM student WHERE stu_id = {student_id}")
    records = cursor.fetchall()
    cursor.execute(
        f" SELECT name FROM grade WHERE grade_id = {int(records[0][3])}")
    name_grade = cursor.fetchall()

    # globle var
    global stu_id_v
    global fname_v
    global lname_v
    global grade_v
    global var_ins_v
    global old_id
    old_id = int(records[0][0])
    stu_id_v.insert(0, records[0][0])
    fname_v.insert(0, records[0][1])
    lname_v.insert(0, records[0][2])
    var_ins_v.set(name_grade[0][0])


def On_edit(p):
    global root
    if p == 1:

        student_edit = Toplevel()
        student_edit.geometry("1720x750")

        Label(student_edit, text="Student ID", font=("", 14, "bold")).grid(
            row=0, column=0, pady=(100, 20), padx=(400, 20))

        Label(student_edit, text="Student ID", font=("", 14, "bold")).grid(
            row=1, column=0, pady=20, padx=(400, 20))

        Label(student_edit, text="Frist name", font=("", 14, "bold")).grid(
            row=2, column=0, pady=20, padx=(400, 20))

        Label(student_edit, text="Last name", font=("", 14, "bold")).grid(
            row=3, column=0, pady=20, padx=(400, 20))

        Label(student_edit, text="Grade", font=("", 14, "bold")).grid(
            row=4, column=0, pady=20, padx=(400, 20))

        Button(student_edit, text="Save Edit", width=45, font=("", 14, "bold"), border=5, command=save_edit_stu).grid(
            row=5, column=0, columnspan=2, pady=20, padx=(400, 20))

        Button(student_edit, text="Viwe Student Information", font=(
            "", 10, "bold"), border=5, command=lambda: View_info(int(stu_id_entry.get()))).grid(row=0, column=2, pady=(100, 20))

        # globle var
        global stu_id_v
        global fname_v
        global lname_v
        global grade_v
        global var_ins_v
        global grdes
        global stu_id_entry

        # school gread
        grdes = [
            "first grade",
            "second grade",
            "therid grade",
            "fourth grade",
            "fifth grade",
            "sixth grade"
        ]

        # varible for option menu
        var_ins_v = StringVar()
        var_ins_v.set("first grade")

        # information need for the student
        stu_id_entry = Entry(student_edit, width=15, font=("", 14, "bold"))
        stu_id_v = Entry(student_edit, width=30, font=("", 14, "bold"))
        fname_v = Entry(student_edit, width=30, font=("", 14, "bold"))
        lname_v = Entry(student_edit, width=30, font=("", 14, "bold"))
        grade_v = OptionMenu(student_edit, var_ins_v, *grdes)
        grade_v.config(font=("", 14, "bold"))

        # position of the entarys and the menuoption
        stu_id_entry.grid(row=0, column=1, pady=(100, 20))
        stu_id_v.grid(row=1, column=1, pady=20, padx=20)
        fname_v.grid(row=2, column=1, pady=20, padx=20)
        lname_v.grid(row=3, column=1, pady=20, padx=20)
        grade_v.grid(row=4, column=1, pady=20, padx=15, sticky=EW)

        student_edit.mainloop()


def On_insert():

    if not stu_id.get() or not fname.get() or not lname.get():
        messagebox.showerror(
            "ERROR", "Make sure you fill all the information")
    else:
        answer = messagebox.askyesno(
            "information", "Are you sure you want to save it?")
        if answer == 1:

            num_grade = grdes.index(var_ins.get()) + 1
            cursor.execute(
                f"INSERT INTO student VALUE ({int(stu_id.get())}, '{fname.get()}', '{lname.get()}', {num_grade})")

            db.commit()

            stu_id.delete(0, END)
            fname.delete(0, END)
            lname.delete(0, END)
            var_ins.set("first grade")


def insert_win(p):

    global root
    if p == 1:
        student_insert = Toplevel()
        student_insert.geometry("1720x750")

        Label(student_insert, text="Student ID", font=("", 14, "bold")).grid(
            row=0, column=0, pady=(100, 20), padx=(400, 20))

        Label(student_insert, text="Frist name", font=("", 14, "bold")).grid(
            row=1, column=0, pady=20, padx=(400, 20))

        Label(student_insert, text="Last name", font=("", 14, "bold")).grid(
            row=2, column=0, pady=20, padx=(400, 20))

        Label(student_insert, text="Grade", font=("", 14, "bold")).grid(
            row=3, column=0, pady=20, padx=(400, 20))

        Button(student_insert, text="Save", width=45, font=("", 14, "bold"), border=5, command=On_insert).grid(
            row=4, column=0, columnspan=2, pady=20, padx=(400, 20))

        # globle var
        global stu_id
        global fname
        global lname
        global grade
        global var_ins
        global grdes

        # school gread
        grdes = [
            "first grade",
            "second grade",
            "therid grade",
            "fourth grade",
            "fifth grade",
            "sixth grade"
        ]

        # varible for option menu
        var_ins = StringVar()
        var_ins.set("first grade")

        # information need for the student
        stu_id = Entry(student_insert, width=30, font=("", 14, "bold"))
        fname = Entry(student_insert, width=30, font=("", 14, "bold"))
        lname = Entry(student_insert, width=30, font=("", 14, "bold"))
        grade = OptionMenu(student_insert, var_ins, *grdes)
        grade.config(font=("", 14, "bold"))

        # position of the entarys and the menuoption
        stu_id.grid(row=0, column=1, pady=(100, 20), padx=20)
        fname.grid(row=1, column=1, pady=20, padx=20)
        lname.grid(row=2, column=1, pady=20, padx=20)
        grade.grid(row=3, column=1, pady=20, padx=15, sticky=EW)

        student_insert.mainloop()


# fun to viwe the information for the student on the screen
def viwe_ifo(p):
    global viwe_screen
    # declarar the window
    viwe_screen = Toplevel()
    viwe_screen.geometry("1720x750")

    # the names for the information for the table
    Label(viwe_screen, text="Student ID", font=("", 14, "bold")).grid(
        row=0, column=0, pady=30, padx=(400, 20))

    Label(viwe_screen, text="First Name", font=("", 14, "bold")).grid(
        row=0, column=1, pady=30, padx=20)

    Label(viwe_screen, text="Last Name", font=("", 14, "bold")).grid(
        row=0, column=2, pady=30, padx=20)

    Label(viwe_screen, text="Grade", font=("", 14, "bold")).grid(
        row=0, column=3, pady=30, padx=20)

    # select the info from the database
    cursor.execute(f" SELECT * FROM student order by grade_id")
    records = cursor.fetchall()

    global i

    # show the info on the screen
    for i in range(len(records)):
        Label(viwe_screen, text=records[i][0], font=("", 12)).grid(
            row=i+1, column=0, pady=10, padx=(400, 20))

        Label(viwe_screen, text=records[i][1], font=("", 12)).grid(
            row=i+1, column=1, pady=10, padx=20)

        Label(viwe_screen, text=records[i][2], font=("", 12)).grid(
            row=i+1, column=2, pady=10, padx=20)

        cursor.execute(
            f" SELECT name FROM grade WHERE grade_id = {int(records[i][3])}")
        name_grade = cursor.fetchall()

        Label(viwe_screen, text=name_grade[0][0], font=("", 12)).grid(
            row=i+1, column=3, pady=10, padx=20)

    # becouse I want to use the fun on delete student
    # I want to put a button on that case
    # so I dont want to use this "viwe_screen.mainloop()"
    if p == 0:
        viwe_screen.mainloop()


# fun when we click on "delete student has the ID" on delete win
def delete_student():

    delete_stu_id = int(delete_stu.get())

    cursor.execute(f"DELETE FROM student WHERE stu_id = {int(delete_stu_id)}")

    delete_stu.delete(0, END)
    db.commit()


# fun when we press the delete button
def on_delete(n):
    if n == 1:
        viwe_screen.destroy()
    viwe_ifo(1)
    global delete_stu
    delete_stu = Entry(viwe_screen, width=20, font=("", 14, "bold"))
    delete_stu.grid(row=i+2, column=0, columnspan=2, pady=30, padx=(350, 20))

    Button(viwe_screen, text="Delete student has the ID", font=("", 14, ""), border=3, command=delete_student).grid(
        row=i+2, column=2, columnspan=3)
    Button(viwe_screen, text="Reload", font=("", 14, ""), border=3, padx=100, command=lambda: on_delete(1)).grid(
        row=i+3, column=1, columnspan=2, sticky=EW)

    viwe_screen.mainloop()


# viwe the marks for the student
def View_marks_stu(p):

    # global win
    global mark_win

    # declar the window to view the marks for the student
    mark_win = Toplevel()
    mark_win.geometry("1720x750")

    # the main Lables on the window
    Label(mark_win, text="Student ID", font=("", 14, "bold")).grid(
        row=0, column=0, padx=(180, 20), pady=50)

    Label(mark_win, text="First name", font=("", 14, "bold")).grid(
        row=0, column=1, padx=(40, 20), pady=50)

    Label(mark_win, text="Last name", font=("", 14, "bold")).grid(
        row=0, column=2, padx=(40, 20), pady=50)

    Label(mark_win, text="Subject", font=("", 14, "bold")).grid(
        row=0, column=3, padx=(40, 20), pady=50)

    Label(mark_win, text="Mark", font=("", 14, "bold")).grid(
        row=0, column=4, padx=(40, 20), pady=50)

    Label(mark_win, text="Grade", font=("", 14, "bold")).grid(
        row=0, column=5, padx=(40, 20), pady=50)

    cursor.execute("""
            SELECT stu_id , fname, lname, title, mark, name
            FROM student st
            JOIN marks m
            ON st.stu_id = m.student_id
            JOIN subject su
            ON su.subject_id = m.subject_id
            JOIN grade g
            ON st.grade_id = g.grade_id
            Order by name

    """)
    reselt = cursor.fetchall()

    # make j global cuz I want to use it on anthor fun
    global j

    for j in range(len(reselt)):
        Label(mark_win, text=reselt[j][0], font=("", 12, "")).grid(
            row=j+1, column=0, padx=(180, 20), pady=20)

        Label(mark_win, text=reselt[j][1].capitalize(), font=("", 12, "")).grid(
            row=j+1, column=1, padx=(40, 20), pady=20)

        Label(mark_win, text=reselt[j][2].capitalize(), font=("", 12, "")).grid(
            row=j+1, column=2, padx=(40, 20), pady=20)

        Label(mark_win, text=reselt[j][3].capitalize(), font=("", 12, "")).grid(
            row=j+1, column=3, padx=(40, 20), pady=20)

        Label(mark_win, text=reselt[j][4], font=("", 12, "")).grid(
            row=j+1, column=4, padx=(40, 20), pady=20)

        Label(mark_win, text=reselt[j][5].capitalize(), font=("", 12, "")).grid(
            row=j+1, column=5, padx=(40, 20), pady=20)
    if p == 1:
        mark_win.mainloop()


# add marks window
def add_mark_win(p):

    def click(*args):
        stu_ID.delete(0, END)

    def click1(*args):
        mark_stu.delete(0, END)

    def save_mark():

        cursor.execute(
            f"SELECT subject_id FROM subject WHERE title = '{sub_var.get()}'")

        reselt = cursor.fetchall()

        cursor.execute(f"""
        INSERT INTO marks(mark, student_id, subject_id)
        VALUE({ int(mark_stu.get()) }, { int(stu_ID.get()) }, {int(reselt[0][0])})
        """)
        add_mark_win(1)

    if p == 1:
        mark_win.destroy()

    View_marks_stu(0)

    stu_ID = Entry(mark_win, border=2, width=15, font=("", 14, "bold"))
    stu_ID.grid(row=j+2, column=0, padx=(180, 20), pady=40)
    stu_ID.insert(0, "Student ID")
    stu_ID.bind("<Button-1>", click)

    mark_stu = Entry(mark_win, border=2, width=15, font=("", 14, "bold"))
    mark_stu.grid(row=j+2, column=1, padx=(20, 20), pady=40)
    mark_stu.insert(0, "Mark")
    mark_stu.bind("<Button-1>", click1)

    cursor.execute("SELECT title from subject")
    titles = cursor.fetchall()

    titles_sub = []
    for i in titles:
        titles_sub.append(i[0])

    sub_var = StringVar()
    sub_var.set(titles_sub[0])

    subject = OptionMenu(mark_win, sub_var, *titles_sub)
    subject.grid(row=j+2, column=3, padx=(20, 20), pady=40)
    subject.config(font=("", 14, "bold"), width=15)

    Button(mark_win, text="Save Student Mark", font=("", 14, "bold"), command=save_mark).grid(
        row=j+2, column=5, padx=(0, 20), pady=40)
    mark_win.mainloop()


# fun when we press the button on the main windows
def On_click(p):

    # Create frame Canvas
    frame = Frame(root, width=200, height=700, bg="#808080")
    frame_canvas = canvas1.create_window(1, 3, anchor="nw", window=frame)

    # create button for control the data
    insert = Button(root, text="Insert", padx=50, font=(
        "", 12), command=lambda: insert_win(p))
    delete = Button(root, text="Delete", padx=45,
                    font=("", 12), command=lambda: on_delete(0))
    edit = Button(root, text="Edit", padx=53, font=(
        "", 12), command=lambda: On_edit(p))
    viwe = Button(root, text="Viwe", padx=49, font=(
        "", 12), command=lambda: viwe_ifo(0))

    add_marks = Button(root, text="Add Mark", padx=31, font=(
        "", 12), command=lambda: add_mark_win(0))

    viwe_marks = Button(root, text="Viwe Mark", padx=28, font=(
        "", 12), command=lambda: View_marks_stu(1))

    # pack the buttons on the canvas
    insert_canvas = canvas1.create_window(25, 100, anchor="nw", window=insert)
    delete_canvas = canvas1.create_window(25, 150, anchor="nw", window=delete)
    edit_canvas = canvas1.create_window(25, 200, anchor="nw", window=edit)
    viwe_canvas = canvas1.create_window(25, 250, anchor="nw", window=viwe)
    add_marks_canvas = canvas1.create_window(
        25, 300, anchor="nw", window=add_marks)
    viwe_marks_canvas = canvas1.create_window(
        25, 350, anchor="nw", window=viwe_marks)


# The main window

img_v1 = Image.open("school.png")
img = ImageTk.PhotoImage(img_v1)


# Create Canvas
canvas1 = Canvas(root, width=1720,
                 height=750)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=img,
                     anchor="nw")

# defane the button on the main window
teacher = Button(root, text="Teacher", padx=30, pady=10,
                 bg="#F08080", font=("", 12, "bold"), fg="white", command=lambda: On_click(0))
student = Button(root, text="Student", padx=30, pady=10,
                 bg="#F08080", font=("", 12, "bold"), fg="white", command=lambda: On_click(1))

button1_canvas = canvas1.create_window(660, 350, anchor="nw", window=teacher)

button2_canvas = canvas1.create_window(660, 420, anchor="nw", window=student)


root.mainloop()
