from connection import get_connection
import tkinter as tk
import tkinter.messagebox as mbox
import sys
import mysql




def marks_main():

    w = tk.Tk()
    w.geometry("300x200")
    w.title("Student Marks")

    def marks_window():
        w1=tk.Tk()
        w1.geometry("300x200")
        w1.title("Marks")
        l1=tk.Label(w1,text="Rollno",font=("Arial",14))
        l2=tk.Label(w1,text="Name",font=("Arial",14))
        l3=tk.Label(w1,text="Subject1",font=("Arial",14))
        l4=tk.Label(w1,text="Subject2",font=("Arial",14))

        e1=tk.Entry(w1,width=10)
        e2=tk.Entry(w1,width=10)
        e3=tk.Entry(w1,width=10)
        e4=tk.Entry(w1,width=10)

        e1.grid(row=1,column=2)
        e2.grid(row=2,column=2)
        e3.grid(row=3,column=2)
        e4.grid(row=4,column=2)

        l1.grid(row=1,column=1)
        l2.grid(row=2,column=1)
        l3.grid(row=3,column=1)
        l4.grid(row=4,column=1)
        


        def save():
            # global e1,e2, e3, e4
            try:
                conn = get_connection()

                cursor = conn.cursor()

                rollno = e1.get()
                name = e2.get()
                sub1 = e3.get()
                sub2 = e4.get()


                cursor.execute("insert into student_marks values(%s, %s, %s,%s)", params=(rollno, name, sub1, sub2))
                conn.commit()

                mbox.showinfo(title="Succcess", message="Successfully saved mark")

                e1.delete(0, tk.END)   #to clear the entry fields after creation
                e2.delete(0, tk.END)
                e3.delete(0, tk.END)
                e4.delete(0, tk.END)

                
            except:
                e = sys.exc_info()
                mbox.showerror(title="Error", message="Something went wrong: {}".format(e[1]))

        button = tk.Button(w1, text="Save", font=("Arial", 14), command=save)
        button.grid(row=5, column=3)


    def find_window():
        w3=tk.Tk()
        w3.geometry("300x200")
        w3.title("Find Result")
        l1=tk.Label(w3,text="Rollno",font=("Arial",14))
        e1=tk.Entry(w3,width=10)
        l1.grid(row=1,column=1)
        e1.grid(row=1,column=2)
        
        def find():
            conn = get_connection()
            c = conn.cursor()
            c.execute("select roll_num,name,sub1,sub2,sub1+sub2 from student_marks where roll_num=%s",params=(e1.get(),))
            row=c.fetchone()
            if row==None:
                mbox.showinfo(title="info",message="Invalid Rollno")
            else:
                result="pass" if row[2]>=40 and row[3]>=40 else "fail"
                a=map(str,row)
                s=" ".join(a)
                s=s+" "+result
                l2=tk.Label(w3,text=s,font=("Arial",14))

                l2.grid(row =2, column=1)
                


        button = tk.Button(w3, text="Find Result", font=("Arial", 14), command=find)
        button.grid(row=3, column=3)

    def on_closing():
        conn = get_connection()
        conn.close()
        w.destroy()



    button1 = tk.Button(w, text="Marks Entry", font=("Arial", 14), command=marks_window)
    button2 = tk.Button(w, text="Find result", font=("Arial", 14), command=find_window)
    
    button1.pack(fill=tk.BOTH, expand=True)
    button2.pack(fill=tk.BOTH, expand = True)

    w.protocol("WM_DELETE_WINDOW", on_closing)



    return w.mainloop()



marks_main()

    