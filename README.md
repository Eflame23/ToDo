# 📝 ToDo App — Django Web Application

A Django-based ToDo application designed to practice real-world web development concepts such as CRUD operations, server-side rendering, and clean frontend–backend separation.  
The project features inline task editing using a popup modal, avoiding unnecessary page navigation and improving user experience.

---

## 🔍 Problem Statement

Most beginner ToDo applications rely on multiple pages for simple operations like editing tasks, leading to poor user experience and redundant navigation.  
This project addresses that by implementing popup-based task editing while keeping backend logic clean and simple.

---

## ✅ Solution Overview

- Built a single-page task dashboard using Django templates  
- Implemented popup-based task editing using JavaScript and CSS  
- Used Django views strictly for data handling, not UI state  
- Maintained a clear separation between UI logic, styling, and backend logic  

---

## 🚀 Features

- Add new tasks  
- Mark tasks as completed  
- Separate lists for pending and completed tasks  
- Edit tasks using a modal popup (no new edit page)  
- Persistent storage using SQLite  
- Clean, dark-themed user interface  

---

## 🧠 Key Technical Concepts Used

- Django Models, Views, and URL routing  
- Django Template Language (DTL)  
- POST-based form handling  
- Hidden form fields for object identification  
- JavaScript-driven UI state (modal open/close)  
- CSS Flexbox and Grid for layout  
- Defensive template rendering using `escapejs`  

---

## 🛠️ Tech Stack

| Layer    | Technology            |
|----------|-----------------------|
| Backend  | Django                |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite                |
| Styling  | Custom CSS            |
| Icons    | Font Awesome          |

---

## 🧩 Architecture & Flow


User opens application
↓
Django view fetches pending and completed tasks from database
↓
Tasks rendered on homepage using Django templates
↓
User actions:
• Add Task → form POST → task saved → redirect home
• Mark Done → request sent → task status updated → redirect home
• Edit Task → popup modal opens → form POST → task updated → redirect home
↓
Updated task lists displayed on page refresh



### 🏗️ Architectural Principles

- Django handles **data storage and business logic**
- Templates handle **HTML rendering**
- JavaScript is used only for **UI interactions (modal open/close)**
- Page refresh ensures UI state resets cleanly after each action

This structure keeps the application:
- Simple
- Predictable
- Easy to debug
- Scalable for future features

