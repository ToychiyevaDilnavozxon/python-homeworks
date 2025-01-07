def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee record added successfully!\n")


def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                print("\nEmployee Records:")
                for record in records:
                    print(record.strip())
            else:
                print("\nNo employee records found.")
    except FileNotFoundError:
        print("\nFile not found. Please add an employee first.")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    try:
        with open("employees.txt", "r") as file:
            for record in file:
                if record.startswith(emp_id):
                    print("\nEmployee Found:")
                    print(record.strip())
                    return
            print("\nEmployee not found.")
    except FileNotFoundError:
        print("\nFile not found. Please add an employee first.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()

        updated = False
        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id):
                    print("\nEmployee Found:")
                    print(record.strip())
                    name = input("Enter new Name (leave blank to keep current): ")
                    position = input("Enter new Position (leave blank to keep current): ")
                    salary = input("Enter new Salary (leave blank to keep current): ")

                    details = record.strip().split(", ")
                    if name:
                        details[1] = name
                    if position:
                        details[2] = position
                    if salary:
                        details[3] = salary

                    file.write(", ".join(details) + "\n")
                    updated = True
                    print("\nEmployee record updated successfully!")
                else:
                    file.write(record)

        if not updated:
            print("\nEmployee not found.")
    except FileNotFoundError:
        print("\nFile not found. Please add an employee first.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()

        with open("employees.txt", "w") as file:
            deleted = False
            for record in records:
                if not record.startswith(emp_id):
                    file.write(record)
                else:
                    deleted = True

            if deleted:
                print("\nEmployee record deleted successfully!")
            else:
                print("\nEmployee not found.")
    except FileNotFoundError:
        print("\nFile not found. Please add an employee first.")


def main():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("\nExiting Employee Records Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
