

# **TaskNest — A Minimal & Efficient Task Management Web App**

TaskNest is a simple, clean, and user-friendly **Django-based To-Do / Task Management application** that helps users create, update, and delete tasks effortlessly. It is designed with a neat UI and follows Django’s best practices using CRUD principles, forms, templates, and proper project structure.

---

##  **Features**

* ✔️ Add new tasks
* ✔️ Edit/update existing tasks
* ✔️ Delete tasks
* ✔️ Mark tasks as done/pending (optional if implemented)
* ✔️ CSRF-protected Django forms
* ✔️ Clean Bootstrap-based UI
* ✔️ Organized code with Django MVT architecture

---

##  **Tech Stack**

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default Django DB)
* **Environment:** Virtualenv / venv

---

##  **Project Structure**

```
TaskNest/
│── manage.py
│── db.sqlite3
│
├── taskapp/
│   ├── migrations/
│   ├── templates/
│   │   └── taskapp/
│   │       ├── home.html
│   │       ├── create.html
│   │       └── update.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py  (optional)
│
└── static/
    └── style.css
```

---

##  **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/TaskNest.git
cd TaskNest
```

### **2. Create Virtual Environment**

```bash
python -m venv myenv
```

### **3. Activate the Environment**

**Windows:**

```bash
myenv\Scripts\activate
```

**Mac/Linux:**

```bash
source myenv/bin/activate
```

### **4. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **5. Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Start Server**

```bash
python manage.py runserver
```

Then open:
 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

##  **How It Works**

1. User lands on the **home page** which lists all tasks.
2. User can **create** a new task using the form.
3. User can **update** a task by clicking the edit button.
4. User can **delete** a task using the delete button.
5. All actions use Django’s MVT pattern.

---

##  **Future Enhancements**

* User Login / Register system
* Task categories
* Due dates & reminders
* Priority levels
* Dark/Light mode
* API endpoints (Django REST Framework)

---

##  **License**

This project is open-source and free to use.


