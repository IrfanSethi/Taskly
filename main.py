from tkinter import *
from tkinter import font
import ttkbootstrap as tb

# ===== Function =====
def speak():
    dueDate = my_date.entry.get()
    duehr = hrbox.get()
    duemin = minbox.get()
    desc = name_widget.get()
    durationhr = hrDuration.get()
    durationmin = minDuration.get()
    priorities = priority.get()
    print(f"\nDesc: {desc}")
    print(f"DueDate: {dueDate}")
    if(int(durationmin) < 10):
        print(f"Duration: {str(durationhr) + ":0" + str(durationmin)}")
    else:
        print(f"Duration: {str(durationhr) + ":" + str(durationmin)}")
    if(int(duemin) < 10):
        print(f"DueTime: {str(duehr) + ":0" + str(duemin)}")
    else:
        print(f"dueTime: {str(duehr) + ":" + str(duemin)}") 
    print(f"Priority: {priorities}")

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

# ===== Tab 1: Home =====
row1 = tb.Frame(tab1)
row1.pack(pady=20)
tb.Label(row1, text="Due Date", font=labelFont).pack(side=LEFT, padx=5, pady=5)

# Define the DateEntry widget here so it is properly scoped.
my_date = tb.DateEntry(row1, bootstyle="danger")
my_date.pack(side=LEFT, padx=5, pady=5)

row2 = tb.Frame(tab1)
row2.pack(pady=20)
tb.Label(row2, text="Enter specific time (Hr-Min)", font=labelFont).pack(side=LEFT, padx=5, pady=5)
hourValue = tb.StringVar()
hrbox = tb.Combobox(row2, textvariable=hourValue, width=5)
hrbox['values'] = [i for i in range(24)]
hrbox.pack(side=LEFT, pady=10, padx=10)

minValue = tb.StringVar()
minbox = tb.Combobox(row2, textvariable=minValue, width=5)
minbox['values'] = [i for i in range(60)]
minbox.pack(side=LEFT, pady=10, padx=10)

row3 = tb.Frame(tab1)
row3.pack(pady=20)
tb.Label(row3, text="Enter task name:", font=labelFont).pack(side=LEFT, padx=5, pady=5)
name_widget = tb.Entry(row3, bootstyle="danger")
name_widget.pack(side=LEFT, pady=10, padx=10)

row4 = tb.Frame(tab1)
row4.pack(pady=20)
tb.Label(row4, text="Enter task duration (Hr-Min):", font=labelFont).pack(side=LEFT, padx=5, pady=5)
hourDuration = tb.StringVar()
hrDuration = tb.Combobox(row4, textvariable=hourDuration, width=5)
hrDuration['values'] = [i for i in range(24)]
hrDuration.pack(side=LEFT, pady=10, padx=10)

minDur = tb.StringVar()
minDuration = tb.Combobox(row4, textvariable=minDur, width=5)
minDuration['values'] = [i for i in range(60)]
minDuration.pack(side=LEFT, pady=10, padx=10)

row5 = tb.Frame(tab1)
row5.pack(pady=20)
tb.Label(row5, text="Enter task priority:", font=labelFont).pack(side=LEFT, padx=5, pady=5)
prioritystuff = tb.StringVar()
priority = tb.Combobox(row5, textvariable=prioritystuff, width=5)
priority['values'] = ["Low",
                      "Med",
                      "High"]
priority.pack(side=LEFT, pady=10, padx=10)

# Button to trigger the speak function
tb.Button(tab1, text="Enter", command=speak).pack(pady=10)

# ===== Tab 2: Tasks =====
output_label_tab2 = tb.Label(tab2, text="", bootstyle="info", wraplength=550, justify=LEFT)
output_label_tab2.pack(pady=20)




# ===== Tab 3: Settings =====
tb.Label(tab3, text="Settings will go here").pack(pady=20)

# Run the app
root.mainloop()
