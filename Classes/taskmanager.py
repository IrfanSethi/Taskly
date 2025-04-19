from Task import Task

class TaskManager:
    def __init__(self):
        self.listtasks = []

    def add(self):
        duration = input("\nHow long is your task? ")
        duedate = input("When is your task due?(MM-DD-YYYY) ")
        priority = input("How important is your task? ")
        description = input("Whats the name of your task?")
        duetime = [5, 10]
        curTask = Task(description, duration, duedate, priority, duetime)

        self.listtasks.append(curTask)

ammarsTask = TaskManager()
ammarsTask.add()        
print(ammarsTask.listtasks)






        
