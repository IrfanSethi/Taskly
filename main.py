from tkinter import *
from tkinter import font
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# Fonts
titleFont = font.Font(family='Helvetica', name='appHighlightFont', size=24, weight='bold')
labelFont = font.Font(family='Helvetica', size=16, weight='bold')

# Window settings
root.title("Calendar")
root.geometry("600x700")

# Title label
mainTitle = tb.Label(root, text="Calendar", font=titleFont)
mainTitle.pack()

# Notebook (tabs)
notebook = tb.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Tabs
tab1 = tb.Frame(notebook)
tab2 = tb.Frame(notebook)
tab3 = tb.Frame(notebook)

notebook.add(tab1, text="Home")
notebook.add(tab2, text="Tasks")
notebook.add(tab3, text="Settings")

# Tab 1: Home
row1 = tb.Frame(tab1)
row1.pack(pady=20)
tb.Label(row1, text="Due Date", font=labelFont).pack(side=LEFT, padx=5, pady=5)
my_date = tb.DateEntry(row1, bootstyle="danger")
my_date.pack(side=LEFT, padx=5, pady=5)


row2 = tb.Frame(tab1)
row2.pack(pady=20)
tb.Label(row2,text = "Enter specific time (Min-Hr) ", font=labelFont).pack(side=LEFT, padx=5, pady=5)
time_widget = tb.Entry(row2,  bootstyle="danger").pack(side=LEFT, pady = 10,padx = 10)

row3 = tb.Frame(tab1)
row3.pack(pady=20)
tb.Label(row3,text = "Enter task name: ", font=labelFont).pack(side=LEFT, padx=5, pady=5)
name_widget = tb.Entry(row3,  bootstyle="danger").pack(side=LEFT, pady = 10,padx = 10)

row4 = tb.Frame(tab1)
row4.pack(pady=20)
tb.Label(row4,text = "Enter task duration: ", font=labelFont).pack(side=LEFT, padx=5, pady=5)
duration_label = tb.Entry(row4,  bootstyle="danger").pack(side=LEFT, pady = 10,padx = 10)

# def speak():
#     my_label.config(text=f"You Entered: {rawDate_entry.get()}")

# rawDate_label = tb.label = tb.Label(row4,text = "Enter How Long The Task Takes: ", font=labelFont).pack(side=LEFT, padx=5, pady=5)
# rawDate_label.pack(pady = 50)
# rawDate_entry = tb.Entry(root)
# rawDate_entry.pack(pady=50)

# mybutton = tb.Button(root,bootstyle="danger outline",text="Enter",command = speak)
# mybutton.pack(pady = 50)

# my_label = tb.Label(root,text="")
# my_label.pack(pady=50)

# Tab 2: Tasks
def speak():
    user_input = enter_task.get()
    output_label.config(text=f'You Typed: {user_input}')

enter_task = tb.Entry(tab2, bootstyle="success")
enter_task.pack(pady=10)

output_label = tb.Label(tab2, text="", bootstyle="info")
output_label.pack(pady=10)

tb.Button(tab2, text="Update", command=speak).pack(pady=10)

# Tab 3: Settings
tb.Label(tab3, text="Settings will go here").pack(pady=20)

# Run the app
root.mainloop()