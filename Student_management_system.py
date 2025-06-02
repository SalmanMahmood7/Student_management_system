FILE = "students.txt"

# Add Student
def add():
    with open(FILE, "a") as f:
        roll = input("Roll no: ")
        name = input("Name: ")
        clas = input("Class: ")
        marks = input("Marks: ")
        f.write(f"{roll},{name},{clas},{marks}\n")
    print("✔ Student Added!\n")

# View All Students
def view():
    try:
        with open(FILE, "r") as f:
            print("\n--- All Student Records ---")
            found = False
            for line in f:
                line = line.strip()
                if line == "":
                    continue  # skip empty lines
                parts = line.split(",")
                if len(parts) == 4:
                    roll, name, clas, marks = parts
                    print(f"Roll: {roll}, Name: {name}, Class: {clas}, Marks: {marks}")
                    found = True
            if not found:
                print("No records to show.\n")
    except FileNotFoundError:
        print("No records file found.\n")

# Search Student by Roll No
def search():
    search_roll = input("Enter Roll to search: ")
    found = False
    try:
        with open(FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue  # skip empty lines
                parts = line.split(",")
                if len(parts) == 4:
                    roll, name, clas, marks = parts
                    if roll == search_roll:
                        print(f"✔ Found: Roll: {roll}, Name: {name}, Class: {clas}, Marks: {marks}")
                        found = True
                        break
    except FileNotFoundError:
        print("No records file found.")

    if not found:
        print("✘ Student not found.\n")

# Update Student
def update():
    update_roll = input("Roll to update: ")
    found = False
    lines = []

    try:
        with open(FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                if len(parts) == 4:
                    roll, name, clas, marks = parts
                    if roll == update_roll:
                        new_name = input("New Name: ")
                        new_class = input("New Class: ")
                        new_marks = input("New Marks: ")
                        lines.append(f"{roll},{new_name},{new_class},{new_marks}\n")
                        found = True
                    else:
                        lines.append(line + "\n")
    except FileNotFoundError:
        print("No student records found.")
        return

    with open(FILE, "w") as f:
        f.writelines(lines)

    print("✔ Student updated!" if found else "✘ Student not found.\n")

# Delete Student
def delete():
    delete_roll = input("Roll to delete: ")
    lines = open(FILE).readlines()
    found = False
    with open(FILE, "w") as f:
        for line in lines:
            roll = line.strip().split(",")[0]
            if roll != delete_roll:
                f.write(line)
            else:
                found = True
    print("✔ Deleted!" if found else "✘ Student not found.\n")

# Main Menu Loop
while True:
    print("\n1. Add  2. View  3. Search  4. Update  5. Delete  6. Exit")
    ch = input("Choice: ")
    if ch == '1':
        add()
    elif ch == '2':
        view()
    elif ch == '3':
        search()
    elif ch == '4':
        update()
    elif ch == '5':
        delete()
    elif ch == '6':
        print("Have a good time!")
        break
    else:
        print("Invalid choice. Try again.\n")
