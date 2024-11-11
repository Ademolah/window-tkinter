from connection import get_connection
import tkinter.messagebox as mbox
import sys


def find_student(rollno):
    conn = get_connection()

    cursor = conn.cursor()
    cursor.execute("select rollno, name, sub1, sub2, sub1+sub2 from student_marks where roll_num=%s", params=(rollno))

    row = cursor.fetchone()
    
    if row == None:
        mbox.showinfo(title="Error", message="Invalid rollno")
    else:
        result = "Pass" if row[2] >= 40 and row[3] >= 40 else "Fail"
        a = map(str, row)
        s = " ".join(a)
        s = s+result

