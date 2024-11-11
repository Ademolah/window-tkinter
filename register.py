import tkinter as tk
import tkinter.messagebox as mbox
from connection import get_connection
import sys
import string
import random


def main():

    def register():
        try:
            conn = get_connection()

            cursor = conn.cursor()

            uid = uid = "2$"+''.join(random.choices(string.ascii_lowercase+string.digits,k=5))
            name = e1.get()
            username = e2.get()
            password = e3.get()

            cursor.execute("insert into user_register values(%s,%s,%s,%s)", params=(uid,name, username, password))
            conn.commit()

            mbox.showinfo(title="Info", message="User registered successfully")

            e1.delete(0, tk.END)   #to clear the entry fields after creation
            e2.delete(0, tk.END)
            e3.delete(0, tk.END)


            conn.close()
        except:
            mbox.showerror(title="Error", message="Error in registering user")
            e = sys.exc_info()
            print(f"Error {e[1]}")


    def close():
        w.destroy()



    w = tk.Tk()
    w.geometry("300x200")
    w.title("Student Register")

    l1 = tk.Label(w, text="Name", font=("Arial", 14))
    l2 = tk.Label(w, text="Username", font=("Arial", 14))
    l3 = tk.Label(w, text="Password", font=("Arial", 14))

    e1 = tk.Entry(w, width=20, font=("Arial", 14))
    e2 = tk.Entry(w, width=20, font=("Arial", 14))
    e3 = tk.Entry(w, width=20, font=("Arial", 14), show="*")


    button1 = tk.Button(w, text="Register", font=("Arial", 14), command=register)
    button2 = tk.Button(w, text="Exit", width=10, font=("Arial", 14), command=close)


    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)
    l3.grid(row=3, column=1)

    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)
    e3.grid(row=3, column=2)
    button1.grid(row=4, column=1)
    button2.grid(row=4, column=2)

    return w.mainloop()

main()