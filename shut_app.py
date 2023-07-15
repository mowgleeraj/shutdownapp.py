import os
import platform
from tkinter import *
from tkinter import messagebox

def execute_shutdown():
    selected_operation = operation_var.get()
    if selected_operation == "Restart":
        restart()
    elif selected_operation == "Restart Time":
        restart_time()
    elif selected_operation == "Log Out":
        logout()
    elif selected_operation == "Shut Down":
        shutdown()
    else:
        messagebox.showerror("Error", "Invalid selection!")

def restart():
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    elif platform.system() == "Darwin":  # macOS
        os.system("sudo shutdown -r now")
    else:
        print("Restart not supported on this platform.")

def restart_time():
    if platform.system() == "Windows":
        os.system("shutdown /r /t 20")
    elif platform.system() == "Darwin":  # macOS
        os.system("sudo shutdown -r +20")
    else:
        print("Restart not supported on this platform.")

def logout():
    if platform.system() == "Windows":
        os.system("shutdown -l")
    elif platform.system() == "Darwin":  # macOS
        os.system("sudo pkill loginwindow")
    else:
        print("Logout not supported on this platform.")

def shutdown():
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    elif platform.system() == "Darwin":  # macOS
        os.system("sudo shutdown -h now")
    else:
        print("Shutdown not supported on this platform.")

# Create the Tkinter application window
st = Tk()
st.title("ShutDown App")
st.geometry("400x200")
st.config(bg="white")

# Create a variable to store the selected operation from the drop-down menu
operation_var = StringVar(st)
operation_var.set("Select Operation")

# Create a drop-down menu to select the operation
operation_menu = OptionMenu(st, operation_var, "Restart", "Restart Time", "Log Out", "Shut Down")
operation_menu.config(font=("Time New Roman", 12), relief=RAISED)
operation_menu.place(x=100, y=50)

# Create a button to execute the selected operation
execute_button = Button(st, text="Execute", font=("Time New Roman", 15, "bold"), relief=RAISED, cursor="plus", command=execute_shutdown)
execute_button.place(x=150, y=120, height=50, width=100)

# Start the Tkinter main loop
st.mainloop()
