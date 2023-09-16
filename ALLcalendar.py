from tkcalendar import Calendar
from tkinter import *
import tkinter.messagebox


master = Tk()

def choice_date():
    present_date = display_cal.get_date()
    user_date = Label(text=present_date)
    user_date.pack(padx=2,pady=2)


display_cal = Calendar(master, setmode="day", date_pattern='d/m/yy')
display_cal.pack(padx=15, pady=15)

def to_do_listx(): 
    child_window=Toplevel()
    child_window.title("Journal")
    child_window.geometry("400x400")
    child_window.configure(bg="#e5ccaa")
    text_label = Label(child_window, text="Your daily Journal")
    text_label.pack()
    my_text_box = Text(child_window, height=10, width=40)
    my_text_box.pack() 
    open_list = Button(child_window,text="Enter To-Do List", command=create_to_do_list)
    open_list.pack()
    open_cal.pack(padx=15,pady=15)



def create_to_do_list(): 
    window2=Toplevel()
    window2.title("To-do list")
    frame_task=Frame(window2)
    frame_task.pack()   
    global listbox_to_do 
    listbox_to_do=Listbox (frame_task,bg="#c1b2ec",fg="white", height=10, width=40,font = "Tahoma")  
    listbox_to_do.pack() 
    enter_task = Button (frame_task, text="Enter Task", command=add_task)
    enter_task.pack()
    delete_button = Button(frame_task, text="Delete Task", command=delete_task)
    delete_button.pack()
    mark_task_done = Button (frame_task,text="Mark tast as done", command=add_checkmark)
    mark_task_done.pack() 


def add_task():
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_to_do.insert(END,input_text)
            listbox_window.destroy()
    listbox_window=Tk()
    listbox_window.title("Add task")
    entry_task=Text(listbox_window,width=40,height=4)
    entry_task.pack()
    button_temp=Button(listbox_window,text="Add task",command=add)
    button_temp.pack()
    listbox_window.mainloop()
  

def delete_task():
    selected_task=listbox_to_do.curselection()
    listbox_to_do.delete(selected_task[0]) 

def add_checkmark():
    selected_indices = listbox_to_do.curselection()
    if selected_indices:
        for index in selected_indices:
            current_text = listbox_to_do.get(index)
            updated_text = current_text + " ✔"
            listbox_to_do.delete(index)
            listbox_to_do.insert(index, updated_text)
 
open_cal = Button(master,text="Select the date", command=to_do_listx)
open_cal.pack(padx=15,pady=15)

master.geometry('800x800')
master.title("GUI CALENDAR")
master.configure(bg="light blue")
master.mainloop()
