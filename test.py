import datetime
while True:
    while True:
        rawDate = input("Enter wheb the task is due (DD-MM-YYYY): ")
        try:
            day, month, year = rawDate.split("-")
        except ValueError:
            print("Incorrect date. Use the [DD-MM-YYYY] format")
            continue
        break
    try:
        dueDate = datetime.datetime(int(year), int(month), int(day))
    except:
        print("Date is incorrect. Please try again.")
        continue
    break


