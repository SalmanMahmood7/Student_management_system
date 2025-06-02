
# Student Manager

A simple Python console application to manage student records with basic functionalities like add, view, search, update, and delete students. Student data is stored persistently in a text file.

---

## 📝 Project Description

This project allows users to manage student information using a command-line interface. The student data includes:

- Roll Number
- Name
- Class
- Marks

The data is saved in a file (`students.txt`) to maintain persistence across program runs.

---

## 🚩 Features

- **Add Student:** Add new student details to the file.
- **View Students:** Display all stored student records.
- **Search Student:** Search for a student by roll number.
- **Update Student:** Modify existing student details.
- **Delete Student:** Remove a student record by roll number.
- **Persistent Storage:** Data is saved in a file for future access.

---

## ⚙️ How to Use

Run the program, then choose an option from the menu by entering the corresponding number:

```

1. Add
2. View
3. Search
4. Update
5. Delete
6. Exit

````

Example:

- Enter `1` to add a new student.
- Enter `3` to search for a student by roll number.
- Enter `6` to exit the program.

---

## 💻 Code Overview

### 1. Add Student

Adds a student record by appending to the file.

```python
def add():
    with open(FILE, "a") as f:
        roll = input("Roll no: ")
        name = input("Name: ")
        clas = input("Class: ")
        marks = input("Marks: ")
        f.write(f"{roll},{name},{clas},{marks}\n")
    print("✔ Student Added!\n")
````

---

### 2. View Students

Reads the file and displays all student records.

```python
def view():
    try:
        with open(FILE, "r") as f:
            for line in f:
                if line.strip():
                    roll, name, clas, marks = line.strip().split(",")
                    print(f"Roll: {roll}, Name: {name}, Class: {clas}, Marks: {marks}")
    except FileNotFoundError:
        print("No records file found.\n")
```

---

### 3. Search Student

Finds and displays a student record by roll number.

```python
def search():
    search_roll = input("Enter Roll to search: ")
    found = False
    try:
        with open(FILE, "r") as f:
            for line in f:
                if line.strip():
                    roll, name, clas, marks = line.strip().split(",")
                    if roll == search_roll:
                        print(f"✔ Found: Roll: {roll}, Name: {name}, Class: {clas}, Marks: {marks}")
                        found = True
                        break
    except FileNotFoundError:
        print("No records file found.")
    if not found:
        print("✘ Student not found.\n")
```

---

### 4. Update Student

Updates a student record by roll number.

```python
def update():
    update_roll = input("Roll to update: ")
    found = False
    lines = []
    try:
        with open(FILE, "r") as f:
            for line in f:
                if line.strip():
                    roll, name, clas, marks = line.strip().split(",")
                    if roll == update_roll:
                        new_name = input("New Name: ")
                        new_class = input("New Class: ")
                        new_marks = input("New Marks: ")
                        lines.append(f"{roll},{new_name},{new_class},{new_marks}\n")
                        found = True
                    else:
                        lines.append(line)
    except FileNotFoundError:
        print("No student records found.")
        return
    with open(FILE, "w") as f:
        f.writelines(lines)
    print("✔ Student updated!" if found else "✘ Student not found.\n")
```

---

### 5. Delete Student

Deletes a student record by roll number.

```python
def delete():
    delete_roll = input("Roll to delete: ")
    found = False
    lines = []
    with open(FILE, "r") as f:
        lines = f.readlines()
    with open(FILE, "w") as f:
        for line in lines:
            roll = line.strip().split(",")[0]
            if roll != delete_roll:
                f.write(line)
            else:
                found = True
    print("✔ Deleted!" if found else "✘ Student not found.\n")
```

---

## 📂 File Storage

* Student records are stored in a text file named `students.txt`.
* Each record is saved on a new line in CSV format:
  `roll,name,class,marks`

---

## 🔄 Program Flow

* The program runs an infinite loop showing the menu.
* It accepts user input to perform different operations.
* Option `6` exits the program.

---

## 📌 Requirements

* Python 3.x
* Basic command-line interface

---

## 🤝 Contribution

Feel free to fork this repository and improve the project. Pull requests and issues are welcome!

---

## 📝 License

This project is open source and free to use.

---
## Author
Made by Salman — A Python developer.


---


