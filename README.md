# Digital Library Management System

## 📌 Project Description
This project is a simple **Digital Library Management System** developed in **Python** using
**Object-Oriented Programming (OOP)** principles.

The goal of this project is to model and manage:
- Books
- Users
- Loans (book borrowing and returning)

No graphical interface or external database is used.
The focus is on **business logic and clean OOP design**.

## 🧩 Project Structure
- src/: Contains all Python source files
- uml/: Contains the UML class diagram

## ⚙️ Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- UML (PlantUML)

## ▶️ How to Run the Project
1. Open a terminal
2. Navigate to the `src` folder:
```bash
cd src
python main.py
## 🧠 UML Design Justification

The system is designed using Object-Oriented Programming principles.

- The **Book** class represents a library resource and stores information such as the book identifier, title, author, and availability.
- The **User** class represents a library member with basic identification information.
- The **Loan** class manages the relationship between a book and a user during a borrowing operation and tracks whether the book has been returned.
- The **Library** class is the central component of the system. It manages books, users, and loans, and enforces the business rules such as borrowing and returning books.

The relationships between classes reflect real-world interactions in a digital library system, ensuring clarity, modularity, and maintainability.

