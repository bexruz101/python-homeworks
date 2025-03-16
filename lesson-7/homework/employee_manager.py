import os


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, "w").close()

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        if self.search_employee(employee_id, silent=True):
            print("Employee ID already exists! Please enter a unique ID.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                records = file.readlines()
                if not records:
                    print("No employee records found.")
                    return
                print("Employee Records:")
                for record in records:
                    print(record.strip())
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self, employee_id=None, silent=False):
        if not employee_id:
            employee_id = input("Enter Employee ID to search: ")
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
            for record in records:
                data = record.strip().split(",")
                if data[0] == employee_id:
                    if not silent:
                        print("Employee Found:")
                        print(record.strip())
                    return record.strip()
        if not silent:
            print("Employee not found.")
        return None

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")
        records = []
        updated = False
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
        with open(self.FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(",")
                if data[0] == employee_id:
                    print("Current Record:", record.strip())
                    name = (
                        input("Enter New Name (leave blank to keep current): ")
                        or data[1]
                    )
                    position = (
                        input("Enter New Position (leave blank to keep current): ")
                        or data[2]
                    )
                    salary = (
                        input("Enter New Salary (leave blank to keep current): ")
                        or data[3]
                    )
                    file.write(f"{employee_id},{name},{position},{salary}\n")
                    updated = True
                else:
                    file.write(record)
        if updated:
            print("Employee record updated successfully!")
        else:
            print("Employee ID not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")
        records = []
        deleted = False
        with open(self.FILE_NAME, "r") as file:
            records = file.readlines()
        with open(self.FILE_NAME, "w") as file:
            for record in records:
                data = record.strip().split(",")
                if data[0] == employee_id:
                    deleted = True
                else:
                    file.write(record)
        if deleted:
            print("Employee record deleted successfully!")
        else:
            print("Employee ID not found.")

    def run(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.run()
