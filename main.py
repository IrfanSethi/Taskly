from tkinter import *
from tkinter import font, messagebox
import ttkbootstrap as tb
from ttkbootstrap.tooltip import ToolTip
import calendar
from datetime import datetime, timedelta, date

# --- Main Application Window ---
root = tb.Window(themename="flatly")
root.title("Taskly")
root.geometry("700x700")
root.resizable(False, False)

# --- Fonts ---
titleFont = font.Font(family='Montserrat', size=28, weight='bold')
labelFont = font.Font(family='Montserrat', size=12, weight='normal')

# Fallback if Montserrat is not available
try:
    font.netamtofont('Montserrat')
except Exception:
    titleFont = font.Font(family='Arial', size=28, weight='bold')
    labelFont = font.Font(family='Arial', size=12, weight='normal')

# --- Task Storage ---
tasks = []

# --- Status Bar ---
status_var = StringVar(value="Welcome to Taskly!")
status_bar = tb.Label(root, textvariable=status_var, bootstyle="secondary inverse", anchor=W, padding=8)
status_bar.pack(side=BOTTOM, fill=X)

# --- Menu Bar ---
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Taskly\nA modern task calendar app."))
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

# --- Title in a Card-like Frame ---
title_frame = tb.Frame(root, bootstyle="info", padding=(20, 10), borderwidth=0)
title_frame.pack(pady=(18, 8), padx=0, fill=X)
tb.Label(title_frame, text="Taskly", font=titleFont, bootstyle="info inverse").pack(anchor=CENTER)

# --- Notebook (Tabs) ---
notebook = tb.Notebook(root, bootstyle="info")
notebook.pack(fill="both", expand=True, padx=0, pady=0)

# --- Tabs ---
tab1 = tb.Frame(notebook, padding=0)
tab2 = tb.Frame(notebook, padding=0)
tab3 = tb.Frame(notebook, padding=0)
notebook.add(tab1, text="Home")
notebook.add(tab2, text="Tasks")
notebook.add(tab3, text="Settings")

# --- Home Tab ---
# Dynamically set the form_container style based on the current theme

def get_form_container_style():
    theme = root.style.theme.name
    if theme == "cyborg":  # Pitch Dark
        return {
            "bootstyle": "dark",
            "padding": (30, 18, 30, 18),
            "borderwidth": 0,
            "relief": "flat"
        }
    elif theme == "darkly":  # Dark
        return {
            "bootstyle": "dark",
            "padding": (30, 18, 30, 18),
            "borderwidth": 0,
            "relief": "flat"
        }
    else:  # Light
        return {
            "bootstyle": "light",
            "padding": (30, 18, 30, 18),
            "borderwidth": 0,
            "relief": "flat"
        }

form_container = tb.Frame(tab1, **get_form_container_style())
form_container.pack(pady=(30, 0), padx=40, fill=None, anchor=CENTER)

form = tb.Frame(form_container)
form.pack()

def update_form_bg():
    pass  # No-op for compatibility

def update_form_container_style():
    style = get_form_container_style()
    form_container.configure(**{k: v for k, v in style.items() if k != 'padding'})
    form_container['padding'] = style['padding']

# Use grid for perfect alignment
row = 0
# Due Date
label_due = tb.Label(form, text="Due Date", font=labelFont, width=16, anchor=E)
label_due.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
my_date = tb.DateEntry(form, bootstyle="info", width=16)
my_date.grid(row=row, column=1, columnspan=2, sticky=W+E, pady=8)
ToolTip(my_date, text="Select the due date for your task.")

row += 1
# Due Time
label_time = tb.Label(form, text="Due Time (Hr:Min)", font=labelFont, width=16, anchor=E)
label_time.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
time_frame = tb.Frame(form)
time_frame.grid(row=row, column=1, columnspan=2, sticky=W, pady=8)
hourValue = tb.StringVar()
hrbox = tb.Combobox(time_frame, textvariable=hourValue, width=6, bootstyle="info")
hrbox['values'] = [f"{i:02d}" for i in range(24)]
hrbox.pack(side=LEFT, padx=(0,5))
minValue = tb.StringVar()
minbox = tb.Combobox(time_frame, textvariable=minValue, width=6, bootstyle="info")
minbox['values'] = [f"{i:02d}" for i in range(60)]
minbox.pack(side=LEFT)
ToolTip(hrbox, text="Select the hour (00-23)")
ToolTip(minbox, text="Select the minute (00-59)")

row += 1
# Task Name
label_name = tb.Label(form, text="Task Name", font=labelFont, width=16, anchor=E)
label_name.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
name_widget = tb.Entry(form, bootstyle="info", width=20)
name_widget.grid(row=row, column=1, columnspan=2, sticky=W+E, pady=8)
ToolTip(name_widget, text="Enter the name of your task.")

row += 1
# Task Duration
label_dur = tb.Label(form, text="Duration (Hr:Min)", font=labelFont, width=16, anchor=E)
label_dur.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
dur_frame = tb.Frame(form)
dur_frame.grid(row=row, column=1, columnspan=2, sticky=W, pady=8)
hourDuration = tb.StringVar()
hrDuration = tb.Combobox(dur_frame, textvariable=hourDuration, width=6, bootstyle="info")
hrDuration['values'] = [f"{i:02d}" for i in range(24)]
hrDuration.pack(side=LEFT, padx=(0,5))
minDur = tb.StringVar()
minDuration = tb.Combobox(dur_frame, textvariable=minDur, width=6, bootstyle="info")
minDuration['values'] = [f"{i:02d}" for i in range(60)]
minDuration.pack(side=LEFT)
ToolTip(hrDuration, text="Duration hours (00-23)")
ToolTip(minDuration, text="Duration minutes (00-59)")

row += 1
# Task Priority
label_pri = tb.Label(form, text="Priority", font=labelFont, width=16, anchor=E)
label_pri.grid(row=row, column=0, sticky=E, pady=8, padx=(0,10))
prioritystuff = tb.StringVar()
priority = tb.Combobox(form, textvariable=prioritystuff, width=16, bootstyle="warning")
priority['values'] = ["Low", "Med", "High"]
priority.grid(row=row, column=1, columnspan=2, sticky=W+E, pady=8)
ToolTip(priority, text="Select the priority of your task.")

# --- Enter Button ---
def add_task():
    dueDate = my_date.entry.get()
    duehr = hrbox.get()
    duemin = minbox.get()
    desc = name_widget.get()
    durationhr = hrDuration.get()
    durationmin = minDuration.get()
    priorities = priority.get()
    if not (desc and dueDate and duehr and duemin and durationhr and durationmin and priorities):
        messagebox.showwarning("Missing Data", "Please fill in all fields.")
        return
    task = {
        "name": desc,
        "due_date": dueDate,
        "due_time": f"{duehr.zfill(2)}:{duemin.zfill(2)}",
        "duration": f"{durationhr.zfill(2)}:{durationmin.zfill(2)}",
        "priority": priorities,
        "status": "Pending"
    }
    tasks.append(task)
    refresh_tasks()
    name_widget.delete(0, END)
    hrbox.set("")
    minbox.set("")
    hrDuration.set("")
    minDuration.set("")
    priority.set("")
    status_var.set("Task added.")

# Make the button fill the width of the form_container and add more vertical space
btn_frame = tb.Frame(form_container, bootstyle="light")
btn_frame.pack(pady=(18, 0), fill=X)
tb.Button(
    btn_frame,
    text="Add Task",
    command=add_task,
    bootstyle="success",
    width=1,  # width is ignored when fill=X
    padding=10
).pack(fill=X, padx=0)

# --- Show Calendar Button and Calendar Window ---
def show_calendar():
    cal_win = tb.Toplevel(root)
    cal_win.title("Calendar - Taskly")
    cal_win.geometry("700x500")
    cal_win.resizable(False, False)

    today = datetime.today()
    current_year = [today.year]
    current_month = [today.month]

    header_frame = tb.Frame(cal_win)
    header_frame.pack(pady=8)

    month_label = tb.Label(header_frame, text="", font=labelFont)
    month_label.pack(side=LEFT, padx=10)

    def update_month_label():
        month_label.config(text=f"{calendar.month_name[current_month[0]]} {current_year[0]}")

    def prev_month():
        if current_month[0] == 1:
            current_month[0] = 12
            current_year[0] -= 1
        else:
            current_month[0] -= 1
        draw_calendar()

    def next_month():
        if current_month[0] == 12:
            current_month[0] = 1
            current_year[0] += 1
        else:
            current_month[0] += 1
        draw_calendar()

    tb.Button(header_frame, text="<", command=prev_month, bootstyle="info").pack(side=LEFT)
    tb.Button(header_frame, text=">", command=next_month, bootstyle="info").pack(side=LEFT)

    cal_frame = tb.Frame(cal_win)
    cal_frame.pack(pady=8, fill=BOTH, expand=True)

    def draw_calendar():
        for widget in cal_frame.winfo_children():
            widget.destroy()
        update_month_label()
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for col, day in enumerate(days):
            tb.Label(cal_frame, text=day, font=labelFont, bootstyle="secondary inverse", width=12).grid(row=0, column=col, padx=2, pady=2)
        month_days = calendar.monthcalendar(current_year[0], current_month[0])
        for row, week in enumerate(month_days, start=1):
            for col, day in enumerate(week):
                box = tb.Frame(cal_frame, bootstyle="light", borderwidth=1, relief="solid", width=120, height=80)
                box.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                box.grid_propagate(False)
                if day == 0:
                    continue
                date_str = f"{current_year[0]}-{current_month[0]:02d}-{day:02d}"
                tb.Label(box, text=str(day), font=("Segoe UI", 10, "bold"), bootstyle="secondary").pack(anchor="nw", padx=4, pady=2)
                # List tasks for this day
                day_tasks = [task for task in tasks if task['due_date'] == date_str]
                if day_tasks:
                    for task in day_tasks[:3]:
                        tb.Label(box, text=f"{task['name']}", font=("Segoe UI", 9), bootstyle="info").pack(anchor="w", padx=6)
                    if len(day_tasks) > 3:
                        tb.Label(box, text=f"+{len(day_tasks)-3} more", font=("Segoe UI", 8), bootstyle="warning").pack(anchor="w", padx=6)
                else:
                    tb.Label(box, text="", font=("Segoe UI", 9)).pack()

    draw_calendar()

# Add the Show Calendar button to the Home tab below the Add Task button
calendar_btn_frame = tb.Frame(form_container, bootstyle="light")
calendar_btn_frame.pack(pady=(6, 0))
tb.Button(
    calendar_btn_frame,
    text="Show Calendar",
    command=show_calendar,
    bootstyle="info",
    width=18,
    padding=6
).pack()

# --- Show Week Calendar Button and Week Calendar Window ---
def show_week_calendar():
    cal_win = tb.Toplevel(root)
    cal_win.title("Week View - Taskly")
    cal_win.geometry("1600x900")  # Even wider and taller for all days and times
    cal_win.resizable(True, True)

    today = datetime.today()
    selected_date = [today]

    header_frame = tb.Frame(cal_win)
    header_frame.pack(pady=8)

    week_label = tb.Label(header_frame, text="", font=labelFont)
    week_label.pack(side=LEFT, padx=10)

    def get_week_dates(center_date):
        # Always start on Sunday
        start = center_date - timedelta(days=center_date.weekday() + 1 if center_date.weekday() < 6 else 0)
        return [start + timedelta(days=i) for i in range(7)]

    def update_week_label():
        week_dates = get_week_dates(selected_date[0])
        week_label.config(text=f"Week of {week_dates[0].strftime('%b %d, %Y')}")

    def prev_week():
        selected_date[0] -= timedelta(days=7)
        draw_week()

    def next_week():
        selected_date[0] += timedelta(days=7)
        draw_week()

    tb.Button(header_frame, text="<", command=prev_week, bootstyle="info").pack(side=LEFT)
    tb.Button(header_frame, text=">", command=next_week, bootstyle="info").pack(side=LEFT)

    cal_frame = tb.Frame(cal_win)
    cal_frame.pack(pady=8, fill=BOTH, expand=True)

    def draw_week():
        for widget in cal_frame.winfo_children():
            widget.destroy()
        update_week_label()
        week_dates = get_week_dates(selected_date[0])
        start_hour = 7
        end_hour = 22
        cell_width = 18  # Set both to 18 for perfect alignment
        # Configure grid weights for even expansion
        for col in range(8):
            cal_frame.grid_columnconfigure(col, weight=1)
        for row in range(end_hour - start_hour + 2):
            cal_frame.grid_rowconfigure(row, weight=1)
        # Header row: days
        tb.Label(cal_frame, text="Time", font=labelFont, bootstyle="secondary inverse", width=cell_width, anchor="center", borderwidth=2, relief="ridge").grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        for col, day_date in enumerate(week_dates):
            day_str = day_date.strftime("%a\n%b %d")
            tb.Label(cal_frame, text=day_str, font=labelFont, bootstyle="secondary inverse", width=cell_width, anchor="center", borderwidth=2, relief="ridge").grid(row=0, column=col+1, padx=1, pady=1, sticky="nsew")
        # Time rows
        for row, hour in enumerate(range(start_hour, end_hour+1), start=1):
            time_str = f"{hour:02d}:00"
            tb.Label(cal_frame, text=time_str, font=labelFont, bootstyle="secondary", width=cell_width, anchor="center", borderwidth=1, relief="ridge").grid(row=row, column=0, padx=0, pady=0, sticky="nsew")
            for col, day_date in enumerate(week_dates):
                date_str = day_date.strftime("%Y-%m-%d")
                cell_tasks = [task for task in tasks if task['due_date'] == date_str and task['due_time'].startswith(f"{hour:02d}")]
                if cell_tasks:
                    text = "\n".join([task['name'] for task in cell_tasks])
                else:
                    text = ""
                tb.Label(cal_frame, text=text, font=("Segoe UI", 9), anchor="nw", borderwidth=1, relief="ridge", width=cell_width, background="#f8f9fa", justify="left").grid(row=row, column=col+1, padx=0, pady=0, sticky="nsew")

    draw_week()

# Replace the previous Show Week button with this one
calendar_btn_frame = tb.Frame(form_container, bootstyle="light")
calendar_btn_frame.pack(pady=(6, 0))
tb.Button(
    calendar_btn_frame,
    text="Show Week",
    command=show_week_calendar,
    bootstyle="info",
    width=18,
    padding=6
).pack()

# --- Tasks Tab: Treeview for displaying tasks ---
columns = ("Task Name", "Due Date", "Due Time", "Duration", "Priority", "Status")
task_tree = tb.Treeview(tab2, columns=columns, show="headings", bootstyle="info")
for col in columns:
    task_tree.heading(col, text=col)
    task_tree.column(col, anchor=CENTER, width=110)
task_tree.pack(fill=BOTH, expand=True, pady=18, padx=18)

def refresh_tasks():
    for row in task_tree.get_children():
        task_tree.delete(row)
    for i, task in enumerate(tasks):
        task_tree.insert("", END, iid=i, values=(
            task["name"],
            task["due_date"],
            task["due_time"],
            task["duration"],
            task["priority"],
            task["status"]
        ))
    status_var.set(f"{len(tasks)} task(s) loaded.")

def delete_task():
    selected = task_tree.selection()
    if not selected:
        messagebox.showinfo("Delete Task", "Please select a task to delete.")
        return
    idx = int(selected[0])
    if messagebox.askyesno("Delete Task", f"Delete task '{tasks[idx]['name']}'?"):
        del tasks[idx]
        refresh_tasks()
        status_var.set("Task deleted.")

def mark_complete():
    selected = task_tree.selection()
    if not selected:
        messagebox.showinfo("Mark Complete", "Please select a task to mark as complete.")
        return
    idx = int(selected[0])
    tasks[idx]["status"] = "Completed"
    refresh_tasks()
    status_var.set("Task marked as completed.")

def on_tree_double_click(event):
    selected = task_tree.selection()
    if not selected:
        return
    idx = int(selected[0])
    task = tasks[idx]
    messagebox.showinfo(
        "Task Details",
        f"Name: {task['name']}\nDue: {task['due_date']} {task['due_time']}\nDuration: {task['duration']}\nPriority: {task['priority']}\nStatus: {task['status']}"
    )

task_tree.bind("<Double-1>", on_tree_double_click)

# --- Task Action Buttons ---
action_frame = tb.Frame(tab2, bootstyle="light")
action_frame.pack(pady=10)
tb.Button(action_frame, text="Delete Task", command=delete_task, bootstyle="danger", width=14, padding=5).pack(side=LEFT, padx=10)
tb.Button(action_frame, text="Mark Complete", command=mark_complete, bootstyle="success", width=14, padding=5).pack(side=LEFT, padx=10)

# --- Settings Tab: Theme Selector ---
# Only show three themes: pitch dark, dark, and light
THEMES = [
    ("Pitch Dark", "cyborg"),   # pitch dark
    ("Dark", "darkly"),         # dark
    ("Light", "flatly")         # light
]

def change_theme(event):
    selected_label = theme_combo.get()
    for label, theme in THEMES:
        if label == selected_label:
            root.style.theme_use(theme)
            status_var.set(f"Theme changed to {label}.")
            update_form_container_style()
            update_form_bg()
            break

tb.Label(tab3, text="Select Theme:", font=labelFont).pack(pady=(18, 5))
theme_combo = tb.Combobox(tab3, values=[label for label, _ in THEMES], width=20, bootstyle="info")
theme_combo.set(THEMES[2][0])  # Default to Light
root.style.theme_use(THEMES[2][1])
theme_combo.pack(pady=8)
theme_combo.bind("<<ComboboxSelected>>", change_theme)

# --- Run the app ---
refresh_tasks()
root.mainloop()
