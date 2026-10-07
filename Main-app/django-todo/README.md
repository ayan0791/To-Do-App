# My Todo List - Django

A simple and user-friendly Todo List web application developed using Django.

This project allows users to add, edit, complete, delete, and clear tasks. The application uses Django's MVT architecture and SQLite database to store the tasks.

## Features

- Add new tasks
- View all tasks
- Edit existing tasks
- Mark tasks as completed
- Delete individual tasks
- Clear all tasks
- Tasks are stored in a database
- Responsive and colorful user interface

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Django Templates

## Project Structure

```text
django-todo/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── .gitignore
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── todo/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    │
    ├── templates/
    │   └── todo/
    │       ├── index.html
    │       └── edit.html
    │
    └── static/
        └── todo/
            └── style.css