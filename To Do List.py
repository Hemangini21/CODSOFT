import tkinter as tk
from tkinter import messagebox
import json

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("600x400")  # Set window size to 600x400

        self.tasks = self.load_tasks()

        self.title_label = tk.Label(master, text="To-Do List", font=("Arial", 20, "bold"), fg="#333")
        self.title_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        self.task_frame = tk.Frame(master, bg="#f0f0f0")
        self.task_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.refresh_tasks()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.add_button.place(relx=0.25, rely=0.75, anchor=tk.CENTER)

        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_task, bg="#FFA500", fg="white", font=("Arial", 12))
        self.edit_button.place(relx=0.75, rely=0.75, anchor=tk.CENTER)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="#FF5733", fg="white", font=("Arial", 12))
        self.delete_button.place(relx=0.25, rely=0.9, anchor=tk.CENTER)

        self.save_button = tk.Button(master, text="Save Tasks", command=self.save_tasks, bg="#007bff", fg="white", font=("Arial", 12))
        self.save_button.place(relx=0.75, rely=0.9, anchor=tk.CENTER)

    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks):
            status = "Complete" if task['completed'] else "Incomplete"
            checkbox = tk.Checkbutton(self.task_frame, text=f"[{task['priority']}] {task['title']} - {status}", font=("Arial", 12), bg="#f0f0f0")
            checkbox.var = tk.BooleanVar(value=task['completed'])
            checkbox.config(variable=checkbox.var, command=lambda index=index: self.toggle_completion(index))
            checkbox.grid(row=index, column=0, sticky="w")

    def add_task(self):
        self.add_edit_window("Add Task")

    def edit_task(self):
        index = self.get_selected_task_index()
        if index is not None:
            self.add_edit_window("Edit Task", index)

    def get_selected_task_index(self):
        selected_index = self.task_frame.grid_slaves()
        if selected_index:
            return selected_index[0].grid_info()['row']
        return None

    def add_edit_window(self, mode, index=None):
        window = tk.Toplevel(self.master)
        window.title(mode)

        title_label = tk.Label(window, text="Title:", font=("Arial", 14), bg="#f0f0f0")
        title_label.grid(row=0, column=0)
        title_entry = tk.Entry(window, width=40, font=("Arial", 12))
        title_entry.grid(row=0, column=1)

        description_label = tk.Label(window, text="Description:", font=("Arial", 14), bg="#f0f0f0")
        description_label.grid(row=1, column=0)
        description_entry = tk.Entry(window, width=40, font=("Arial", 12))
        description_entry.grid(row=1, column=1)

        deadline_label = tk.Label(window, text="Deadline (YYYY-MM-DD):", font=("Arial", 14), bg="#f0f0f0")
        deadline_label.grid(row=2, column=0)
        deadline_entry = tk.Entry(window, width=40, font=("Arial", 12))
        deadline_entry.grid(row=2, column=1)

        priority_label = tk.Label(window, text="Priority:", font=("Arial", 14), bg="#f0f0f0")
        priority_label.grid(row=3, column=0)
        priority_entry = tk.Entry(window, width=40, font=("Arial", 12))
        priority_entry.grid(row=3, column=1)

        if mode == "Edit Task":
            task = self.tasks[index]
            title_entry.insert(tk.END, task['title'])
            description_entry.insert(tk.END, task['description'])
            deadline_entry.insert(tk.END, task['deadline'])
            priority_entry.insert(tk.END, task['priority'])

        save_button = tk.Button(window, text="Save", command=lambda: self.save_task(window, mode, index, title_entry.get(), description_entry.get(), deadline_entry.get(), priority_entry.get()), bg="#007bff", fg="white", font=("Arial", 12))
        save_button.grid(row=4, column=0, columnspan=2, pady=5)

    def save_task(self, window, mode, index, title, description, deadline, priority):
        if title and description and deadline and priority:
            if mode == "Add Task":
                self.tasks.append({'title': title, 'description': description, 'deadline': deadline, 'priority': priority, 'completed': False})
            else:
                self.tasks[index] = {'title': title, 'description': description, 'deadline': deadline, 'priority': priority, 'completed': self.tasks[index]['completed']}
            self.refresh_tasks()
            window.destroy()
        else:
            messagebox.showwarning("Incomplete Information", "Please fill all the fields.")

    def delete_task(self):
        index = self.get_selected_task_index()
        if index is not None:
            del self.tasks[index]
            self.refresh_tasks()

    def toggle_completion(self, index):
        self.tasks[index]['completed'] = not self.tasks[index]['completed']
        self.refresh_tasks()

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
