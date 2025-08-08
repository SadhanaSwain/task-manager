Task Manager

A Task Manager Application built with Python and Django for creating, managing, and tracking tasks efficiently. This project demonstrates full-stack development skills, including backend logic, database integration, and CRUD (Create, Read, Update, Delete) operations.

🚀 Features

Add, update, and delete tasks

Mark tasks as completed

View pending and completed tasks

User-friendly interface

Database-driven storage for persistent data


🛠 Tech Stack

Backend: Python, Django

Database: SQLite (default) / MySQL (optional)

Version Control: Git & GitHub


📂 Project Structure

task_manager/
│
├── task_manager/       # Main Django project folder
├── tasks/              # Django app for task management
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── db.sqlite3          # Database file (default)
├── manage.py           # Django management script
└── README.md           # Project documentation

⚙ Installation & Setup

1. Clone the Repository

git clone https://github.com/SadhanaSwain/task-manager.git
cd task-manager


2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate      # For Mac/Linux
venv\Scripts\activate         # For Windows


3. Install Dependencies

pip install -r requirements.txt


4. Apply Migrations

python manage.py migrate


5. Run the Development Server

python manage.py runserver


6. Access the Application Open your browser and go to:

http://127.0.0.1:8000/

[GitHub](https://github.com/SadhanaSwain/task-manager)



📌 Usage

Create a task by filling out the form.

Edit or delete tasks as needed.

Mark tasks as completed to keep your list organized.

Contributing

Contributions are Welcome! Please fork the repository and submit a pull request.
