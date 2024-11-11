import tkinter as tk
import tkinter.messagebox as mbox
from connection import get_connection



def main_login():


    def login():
        try:

            conn = get_connection()
            cursor = conn.cursor()

            username = e1.get().lower()
            password = e2.get()

            cursor.execute("select * from user_register where username=%s and password=%s",params=(username, password))

            row = cursor.fetchone()

            if row == None:
                mbox.showinfo(title="Error", message="Invalid username or password")
            else:
                mbox.showinfo(title="Success", message="Welcome to cloudity")

        except:
            mbox.showerror(title="Error", message="Error logging in")


    def close():
        w.destroy()


    w = tk.Tk()
    w.geometry("300x200")
    w.title("Login")

    l1 = tk.Label(w, text="Username", font=("Arial", 14))
    l2 = tk.Label(w, text="Password", font=("Arial", 14))

    e1 = tk.Entry(w, width=17, font=("Arial", 14))
    e2 = tk.Entry(w, width=17, font=("Arial", 14), show="*")

    button = tk.Button(w, text="Login", font=("Arial", 14), command=login)
    button2 = tk.Button(w, text="Exit", font=("Arial", 14), command=close)

    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)

    e1.grid(row=1, column=2)
    e2.grid(row=2, column=2)

    button.grid(row=4, column=2)
    button2.grid(row=4, column=1)


    return w.mainloop()



main_login()