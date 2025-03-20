import json
import csv

# Step 1: Create and write the initial tasks.json file
tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1},
]

# Writing tasks.json
with open("tasks.json", "w") as file:
    json.dump(tasks_data, file, indent=4)


# Step 2: Load tasks from tasks.json
def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)


tasks = load_tasks()


# Step 3: Display tasks
def display_tasks(tasks):
    print("\nTask List:")
    print(f"{'ID':<5} {'Task Name':<20} {'Completed':<10} {'Priority':<10}")
    print("=" * 50)
    for task in tasks:
        print(
            f"{task['id']:<5} {task['task']:<20} {task['completed']:<10} {task['priority']:<10}"
        )


display_tasks(tasks)


# Step 4: Save modified tasks back to JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Step 5: Task Completion Statistics
def task_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = (
        sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0
    )

    print("\nTask Completion Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {round(avg_priority, 2)}")


task_statistics(tasks)


# Step 6: Convert JSON Data to CSV
def convert_json_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])  # Header
        for task in tasks:
            writer.writerow(
                [task["id"], task["task"], task["completed"], task["priority"]]
            )

    print(f"\nCSV file '{filename}' has been created successfully.")


convert_json_to_csv(tasks)
