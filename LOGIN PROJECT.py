from tkinter import *
from tkinter import messagebox
import csv
import sys
import threading
import subprocess
def check():
    usr=login_entry.get()
    password=passw_entry.get()
    with open("login.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
              if(len(row)>=2 and row[0].strip()==usr and row[1].strip()==password):
                          messagebox.showinfo(title="Success Message",message="Login Succesfully")
                          subprocess.Popen([sys.executable,"PROJECT 3.py"],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                          break
        else:
           messagebox.showerror(title="Failure message",message="Login Failed!,Check Username and Password")
    login_entry.delete(0,END)
    passw_entry.delete(0,END)
    window.destroy()
    
window=Tk()
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
icon=PhotoImage(file='SKCET LOGO.png')
window.iconphoto(True,icon)
window.config(bg="black")
window.title("SKCET")

main_icon=PhotoImage(file='SKCET Main.png')
main_label=Label(image=main_icon,bg="black")
main_label.pack(pady=20)

main_frame=Frame(window,bg="grey",width=1000,height=1000)
main_frame.pack(padx=100,pady=20)

login_label=Label(main_frame,text="User-Id",font=("Bold",20),bg="grey",fg="white")
login_label.grid(row=0,column=0)

login_entry=Entry(main_frame,width=50)
login_entry.grid(row=1,column=0,pady=10,padx=40)

passw_label=Label(main_frame,text="Password",font=("Bold",20),bg="grey",fg="white")
passw_label.grid(row=2,column=0,pady=10,padx=40)

passw_entry=Entry(main_frame,show="*",width=40)
passw_entry.grid(row=3,column=0,pady=10,padx=40)

login_button=Button(main_frame,text="Login",fg="white",bg="blue",font=("Bold",20),command=check)
login_button.grid(row=4,column=0,pady=10,padx=40)

main_frame2=Frame(window,bg='grey')
main_frame2.pack(padx=100)

signup1=Label(main_frame2,text="I don't have an account",fg="white",bg="grey",font=("Bold",10),compound='right')
signup1.grid(row=0,column=0)

signup2=Button(main_frame2,text="Sign Up",font=("Bold",10),bg='grey',fg='blue',border=0)
signup2.grid(row=0,column=1)


window.mainloop()
