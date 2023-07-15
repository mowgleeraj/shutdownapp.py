from tkinter import *
import os

def restart():
    os.system("Shutdown /r /t 1")
def restart_time():
    os.system("Shutdown /r /t 20")
def logout():
    os.system("Shutdown -l")
def shutdown():
    os.system("sudo shutdown -h now")

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="black")

r_button = Button (st,text="Restart",font=("Time New Roman",15,"bold"),relief=RAISED,cursor="plus",command=restart())
r_button.place(x=180,y=80,height=50,width=115)

rt_button = Button (st,text="Restart Time",font=("Time New Roman",15,"bold"),relief=RAISED,cursor="plus",command=restart_time())
rt_button.place(x=180,y=150,height=50,width=115)

lg_button = Button (st,text="Log Out",font=("Time New Roman",15,"bold"),relief=RAISED,cursor="plus",command=logout())
lg_button.place(x=180,y=220,height=50,width=115)

st_button = Button (st,text="ShutDown",font=("Time New Roman",15,"bold"),relief=RAISED,cursor="plus",command=shutdown())
st_button.place(x=180,y=290,height=50,width=115)


st.mainloop()
