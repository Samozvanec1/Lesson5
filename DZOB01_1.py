import tkinter as tk
class  Task():

    def __init__(self, vvod, srok_do):
        self.vvod = vvod
        self.srok_do = srok_do
        self.status_rez = False

    def mark_as_status_rez(self):
        self.status_rez = True

    def __str__(self):
        return f"{self.vvod} (Сделать до: {self.srok_do}) - {'Готово' if self.status_rez else 'Ещё выполняется'}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, vvod, srok_do):
        self.tasks.append(Task(vvod, srok_do))

    def mark_task_status_rez(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_status_rez()
    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status_rez]
        if not current_tasks:
            print("Неверный список")
        else:
            for task in current_tasks:
                print(task)
    def show_end_tasks(self):
        end_tasks = [task for task in self.tasks if task.status_rez]
        if not end_tasks:
            print("Неверный список")
        else:
            for task in end_tasks:
                print(task)



task_manager = TaskManager()
task_manager.add_task("Сделать Д/З со списком", "10.05.24.")
task_manager.add_task("Дать яблоко Белоснежке", "01.05.24.")
task_manager.add_task("Разговорить Ариэль", "07.05.24.")
task_manager.add_task("Переловить мышей в доме у Золушки", "04.05.24.")

print("Текущие задачи:")
task_manager.show_current_tasks()



task_manager.mark_task_status_rez(2)
task_manager.mark_task_status_rez(0)

print("\nоставшиеся текущие задачи")
task_manager.show_current_tasks()

print("\n Успешно сделанные задачи")

task_manager.show_end_tasks()
