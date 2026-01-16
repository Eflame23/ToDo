# 📝 ToDo App — Django Web Application

A Django-based ToDo application built to practice real-world web development concepts such as CRUD operations, server-side rendering, and clean separation between frontend and backend logic.

The application includes **inline task editing using a popup modal**, allowing users to update tasks without navigating to a new page, resulting in a smoother and more modern user experience.

---

## 🔍 Problem Statement

Many beginner-level ToDo applications rely on multiple pages for basic actions such as editing tasks. This leads to unnecessary navigation, poor user experience, and tightly coupled UI and backend logic.

This project addresses that problem by implementing **popup-based task editing** while keeping the backend logic simple, readable, and scalable.

---

## ✅ Solution Overview

- Built a single-page task dashboard using Django templates  
- Implemented popup-based task editing using JavaScript and CSS  
- Used Django views strictly for data handling and database updates  
- Maintained a clear separation between UI logic, styling, and backend logic  

---

## 🚀 Features

- Add new tasks  
- Mark tasks as completed  
- View pending and completed tasks in separate sections  
- Edit tasks using a modal popup (no separate edit page)  
- Persistent data storage using SQLite  
- Clean, dark-themed user interface  

---

## 🧠 Key Technical Concepts Used

- Django Models, Views, and URL routing  
- Django Template Language (DTL)  
- POST-based form handling  
- Hidden form fields for object identification  
- JavaScript-driven UI interactions (popup open/close)  
- CSS Flexbox and Grid for layout  
- Safe template-to-JavaScript data handling using `escapejs`  

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Django |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Styling | Custom CSS |
| Icons | Font Awesome |

---

## ▶️ How to Run This Project Locally

Follow these steps to download and run the project on your system.

### 1. Clone the Repository
```bash
git clone <repository-url>
```

### 2. Navigate to the Project Folder
```bash
cd ToDo-App
```

### 3. Create a Virtual Environment
```bash
python -m venv env
```

### 4. Activate the Virtual Environment

Windows
```bash
env\Scripts\activate
```

macOS / Linux
```bash
source env/bin/activate
```

### 5. Install Dependencies
```bash
pip install django
```

### 6. Apply Database Migrations
```bash
python manage.py migrate
```

### 7. Start the Development Server
```bash
python manage.py runserver
```

### 8. Open in Browser
```bash
http://127.0.0.1:8000/
```

---

### 📌 Learning Outcomes

Built a complete CRUD-based web application using Django

Gained practical experience with Django templates and views

Learned how to manage UI behavior using JavaScript without frameworks

Understood form handling, POST requests, and redirects

Debugged common Django errors such as NoReverseMatch

Improved understanding of frontend–backend separation

---

### 🔮 Future Improvements

AJAX-based editing (no page refresh)

User authentication

Task prioritization and due dates

REST API version of the application

Improved mobile responsiveness

---

### 👤 Author

Eshan Manoj | 
B.Tech Student | Aspiring Software Engineer
