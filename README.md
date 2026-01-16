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

ARCHITECTURE & FLOW – TODO APP (DJANGO)

The application follows a simple request–response architecture.
Django handles all backend logic and database operations, while
JavaScript is used only for UI interactions such as opening and
closing the edit popup.

------------------------------------------------------------

## 🧩 APPLICATION FLOW

User opens the application
|
v
Django view fetches pending and completed tasks from the database
|
v
Tasks are rendered on the homepage using Django templates
|
v
User performs actions:

- Add Task
  -> Form POST request
  -> Task saved in database
  -> Redirect to home page

- Mark Task as Done
  -> Request sent with task ID
  -> Task status updated in database
  -> Redirect to home page

- Edit Task
  -> Edit button clicked
  -> Popup modal opens (handled by JavaScript)
  -> User submits edited task
  -> Form POST request with task ID and updated text
  -> Task updated in database
  -> Redirect to home page

|
v
Updated task lists are displayed after page refresh

------------------------------------------------------------

### ARCHITECTURAL PRINCIPLES

- Django manages data storage, business logic, and routing
- Templates handle server-side HTML rendering
- JavaScript is used only for UI behavior (popup open/close)
- POST requests are used for all data-modifying actions
- Page refresh resets UI state after each operation

This design keeps the application simple, predictable,
easy to debug, and scalable for future improvements.


