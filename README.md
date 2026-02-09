# Research LIMS Sample Registry

A lightweight Laboratory Information Management System (LIMS) prototype built with Django for managing research samples. This project demonstrates core LIMS concepts such as sample tracking, data validation, and secure data management using the Django ORM.

## Features

- **Sample Management:** Track samples with unique IDs, types, collection dates, and status.
- **Sample Lifecycle:** Supports statuses: Collected → Processing → Stored → Archived.
- **Data Validation:** Enforces unique sample IDs and valid choices for types and status.
- **Admin Interface:** Full CRUD via Django Admin for rapid testing and management.
- **Future Enhancements:** Role-based access control (RBAC), automated tests, EDC/clinical data integration, and AI-assisted anomaly detection.

## Tech Stack

- Python 3.x
- Django (Django ORM)
- SQLite (default, can switch to PostgreSQL)
- HTML/CSS via Django Admin (for admin interface)

## How to Run

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   py -m venv venv
   venv\Scripts\Activate
3. Install dependencies:
   pip install django
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Create superuser for admin access:
   python manage.py createsuperuser
6. Start server:
   python manage.py runserver
7. Access Django Admin:
   http://127.0.0.1:8000/admin

## Project Purpose

This mini-project is ideal for demonstrating:

- Django ORM usage for relational data
- Sample lifecycle and workflow management
- Preparation for adding RBAC, automated tests, EDC/clinical data handling, and AI-assisted anomaly detection