# 🧑‍💼 Staff Profile Management System

A **Django-based web application** that allows organizations to **create, view, update, and delete staff profiles**, with authentication features for secure access and management.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Secure login and logout system using Django's built-in authentication.
  - Only authenticated users can create, update, or delete staff profiles.

- 👥 **Staff Management**
  - Add new staff profiles easily.
  - Edit and delete staff details.
  - View all staff in a clean, organized list.

- 🧾 **Profile Details**
  - View individual staff profiles with full details.
  - Simple, responsive design for easy navigation.

- ⚙️ **Admin Functionality**
  - Fully integrated with the Django Admin panel for backend management.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite (default Django database)
- **Authentication:** Django built-in User model
- **Version Control:** Git & GitHub

---

## 🧩 Project Structure

Staff-Profile/
│
├── staffapp/
│ ├── migrations/
│ ├── templates/
│ │ ├── login_page.html
│ │ ├── staffs.html
│ │ ├── create_staff_profile.html
│ │ ├── update_profile_page.html
│ │ ├── delete_profile.html
│ │ └── profile_page.html
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── manage.py
├── db.sqlite3
└── README.md

yaml


---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/adelana107/Staff-Profile.git
   cd Staff-Profile
Create and activate a virtual environment

bash

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On macOS/Linux
Install dependencies

bash

pip install -r requirements.txt
Run database migrations

bash
Copy code
python manage.py migrate
Create a superuser

bash

python manage.py createsuperuser
Run the development server

bash

python manage.py runserver
Open in your browser

cpp

http://127.0.0.1:8000/
🌱 What I Learned
While building this project, I learned to:

Work with Django’s Model-View-Template (MVT) structure effectively.

Use Django forms to handle data creation and updates securely.

Implement user authentication and authorization with login restrictions.

Manage CRUD operations for database models.

Organize reusable templates and apply Django’s message framework for feedback.

Deploy clean, readable code that follows Django best practices.

This project strengthened my understanding of backend logic, form validation, and user session handling in Django.

👨‍💻 Author
Adelana Oluwafunmibi
Backend Engineer | Django | Python | REST APIs
🛰️ Orbiting around good ideas
📧 adelana787898@gmail.com
🔗 GitHub Profile
