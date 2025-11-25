import csv
import os

FILE_NAME = "students.csv"



def setup_file():# Create the file with headers if it doesn't exist
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Class", "Age"])


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    student_class = input("Enter Class: ")
    age = input("Enter Age: ")

    
    with open(FILE_NAME, "r") as f: # Checks duplicate ID
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if row[0] == student_id:
                print("❌ Student with this ID already exists!")
                return

   
    with open(FILE_NAME, "a", newline="") as f:  # Writes new record
        writer = csv.writer(f)
        writer.writerow([student_id, name, student_class, age])

    print("✔ Student added successfully!")
def search_student():
    student_id = input("Enter Student ID to search: ")

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == student_id:
                print("\n--- Student Found ---")
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Class: {row[2]}")
                print(f"Age: {row[3]}")
                return

    print("❌ No student found with that ID.")
def delete_student():
    student_id = input("Enter Student ID to delete: ")

    records = []
    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == student_id:
                found = True
            else:
                records.append(row)

    if not found:
        print("❌ Student not found.")
        return

    # Write updated list back
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(records)

    print("✔ Student deleted successfully!")
def main():
    setup_file()
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search_student()

        elif choice == "3":
            delete_student()

        elif choice == "4":
            print("👋 Exiting...")
            break

        else:
            print("⚠ Invalid choice! Try again.")
if __name__ == "__main__":
    main()
