# Library_Management_System

This is a web-based Library Management System (LMS) application built with Django that allows users to perform CRUD (Create, Read, Update, Delete) operations on library resources. With this application, you can efficiently manage the library's collection of books.

Book Management:
Create, update, and delete book records.
view all book details.
Manage book categories and authors.

Installation

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

Set up the database: 
python manage.py makemigrations
python manage.py migrate

Create a superuser (an admin account):
python manage.py createsuperuser

Start the development server:
python manage.py runserver

