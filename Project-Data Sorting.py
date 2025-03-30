from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("CALENDAR")
root.geometry("500x350")
my_date = tb.DateEntry(root,bootstyle = "danger")
my_date.pack(pady=50)

name_widget = tb.Entry()
name_widget.pack(pady = 20)
due_widget = tb.Entry()
due_widget.pack(pady = 20)
duration_widget = tb.Entry()
duration_widget.pack(pady = 20)

root.mainloop()

import datetime

def date_entry():
    while True:
        while True:
            rawDate = input("Enter when the task is due (hrs-min-DD-MM-YYYY): ")
            try:
                hrs, min, day, month, year = rawDate.split("-")
            except ValueError:
                print("Incorrect date. Use the [hrs-min-DD-MM-YYYY] format")
                continue
            break
        try:
            dueDate = datetime.datetime(int(year), int(month), int(day), int(hrs), int(min))
        except:
            print("Date is incorrect. Please try again.")
            continue
        break
    return dueDate


class Task:
    def __init__(self):
        self.name = input("Task name: ")
        self.dueDate = date_entry()
        self.priority = input("Enter the priority(High/Med/Low): ")



task1 = Task()
print(task1.name)
print(task1.dueDate)
