import os

# Check if the "employees.txt" file exists, if not, create it with a header
if not os.path.exists("employees.txt"):
    with open("employees.txt", "w") as file:
        file.write("Employee ID, Name, Position, Salary\n")  # Write the column headers


# Function to add a new employee record to the file
def add_new_employee():
    with open("employees.txt", "a") as file:  # Open file in append mode
        id = int(input("Enter id: "))  # Get employee ID as an integer
        name = input("Enter name: ")  # Get employee name
        position = input("Enter position: ")  # Get employee position
        salary = int(input("Enter salary: "))  # Get employee salary as an integer
        file.write(f"{id},{name},{position},{salary}\n")  # Write data to file


# Function to search for an employee by ID
def search_employee():
    id = input("Enter Employee ID to search: ")  # Get the ID to search
    with open("employees.txt", "r") as file:
        records = file.readlines()  # Read all lines from the file
        for record in records[1:]:  # Skip the first line (header)
            details = record.split(",")  # Split each record into a list
            if details[0] == id:  # Check if ID matches
                print(
                    f"\nEmployee Found: ID={details[0]}\nName={details[1]}\nPosition={details[2]}\nSalary={details[3]}\n"
                )
                return  # Exit function once found
    print("Employee ID not found!\n")  # If not found, print message


# Function to update employee information
def update_employee():
    id = input("Enter Employee ID to update: ")  # Get the ID to update
    updated_records = []
    found = False

    with open("employees.txt", "r") as file:
        records = file.readlines()  # Read all lines

    for record in records:
        details = record.split(",")  # Split record into list
        if details[0] == id:  # If ID matches
            found = True
            print(
                f"Current details: Name={details[1]}, Position={details[2]}, Salary={details[3]}"
            )
            # Get new details, keep existing ones if user presses Enter
            name = input("Enter new Name (or press Enter to keep unchanged): ") or details[1]
            position = input("Enter new Position (or press Enter to keep unchanged): ") or details[2]
            salary = input("Enter new Salary (or press Enter to keep unchanged): ") or details[3]
            updated_records.append(f"{id}, {name}, {position}, {salary}\n")  # Add updated record
            print("Employee details updated successfully!\n")
        else:
            updated_records.append(record)  # Keep existing records unchanged

    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)  # Write updated records back to file
    else:
        print("Employee ID not found!\n")  # If ID was not found


# Function to delete an employee by ID
def delete_employee():
    id = input("Enter Employee ID to delete: ")  # Get ID to delete
    updated_records = []
    found = False

    with open("employees.txt", "r") as file:
        records = file.readlines()  # Read all lines

    for record in records:
        details = record.split(",")  # Split record into list
        if details[0] == id:  # If ID matches, mark for deletion
            found = True
            print(f"Employee {id} deleted successfully!\n")
        else:
            updated_records.append(record)  # Keep other records unchanged

    if found:
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)  # Write remaining records to file
    else:
        print("Employee ID not found!\n")  # If ID was not found


# Main program logic - ask user for a choice
try:
    choice = int(
        input(
            """1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit: \n"""
        )
    )

    if choice == 1:
        add_new_employee()  # Call function to add new employee
    elif choice == 2:
        with open("employees.txt", "r") as file:  # Open file in read mode
            all_records = file.read()
            print(all_records)  # Print all employee records
    elif choice == 3:
        search_employee()  # Call function to search employee
    elif choice == 4:
        update_employee()  # Call function to update employee
    elif choice == 5:
        delete_employee()  # Call function to delete employee
    elif choice == 6:
        print("Exiting program. Goodbye!")  # Exit message
    else:
        print("Invalid choice. Please enter a valid option.\n")  # Handle invalid input

except Exception as e:
    print(e)  # Print any errors that occur
