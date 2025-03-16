import json
import csv
import os
from abc import ABC, abstractmethod


class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass


class JSONStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4)

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            return json.load(file)


class CSVStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow(task.values())

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]


class TaskManager:
    def __init__(self, storage_strategy, filename):
        self.filename = filename
        self.storage = storage_strategy
        self.tasks = self.storage.load(self.filename)

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        self.tasks.append(
            {
                "Task ID": task_id,
                "Title": title,
                "Description": description,
                "Due Date": due_date,
                "Status": status,
            }
        )
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task["Task ID"] == task_id:
                task["Title"] = (
                    input(f"Enter new title ({task['Title']}): ") or task["Title"]
                )
                task["Description"] = (
                    input(f"Enter new description ({task['Description']}): ")
                    or task["Description"]
                )
                task["Due Date"] = (
                    input(f"Enter new due date ({task['Due Date']}): ")
                    or task["Due Date"]
                )
                task["Status"] = (
                    input(f"Enter new status ({task['Status']}): ") or task["Status"]
                )
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task["Task ID"] != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter status to filter by (Pending/In Progress/Completed): ")
        filtered = [task for task in self.tasks if task["Status"] == status]
        if not filtered:
            print("No tasks found with that status.")
        else:
            for task in filtered:
                print(task)

    def save_tasks(self):
        self.storage.save(self.tasks, self.filename)
        print("Tasks saved successfully!")

    def run(self):
        while True:
            print("\nTo-Do Application")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    format_choice = input("Choose file format (json/csv): ").strip().lower()
    filename = "tasks.json" if format_choice == "json" else "tasks.csv"
    storage = JSONStorage() if format_choice == "json" else CSVStorage()
    manager = TaskManager(storage, filename)
    manager.run()
