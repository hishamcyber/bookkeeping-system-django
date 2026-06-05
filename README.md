# 📘 Bookkeeping System (Django)

A web-based **Bookkeeping System** built with Django that allows users to track income and expenses, organize transactions using categories, and view financial statistics through a dashboard.

Each user has their own isolated data for security and privacy.

---

# 🚀 Features

* User authentication (Register / Login / Logout)
* Income & Expense tracking
* Main & Sub Category system
* Personal financial dashboard
* Automatic balance calculation
* Record filtering (income, expense, category-based)
* User data isolation (each user sees only their data)

---

# 🛠️ Tech Stack

* Backend: Django (Python)
* Database: PostgreSQL / SQLite (development)
* Frontend: HTML, CSS, JavaScript
* ORM: Django ORM

---

# ⚙️ Installation

## 1. Clone project

```bash
git clone <your-repo-url>
cd BookkeepingSystem
```

## 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run migrations

```bash
python manage.py migrate
```

## 5. Create superuser

```bash
python manage.py createsuperuser
```

## 6. Run server

```bash
python manage.py runserver
```

---

# 👤 Default Test Accounts

### Admin

```
username: bookadmin
password: bookadmin
```

### User

```
username: bookuser
password: adminadmin123
```

---

# 🧱 Database Design

## User

(Django built-in authentication system)

---

## MainCategory

* id
* name
* user (ForeignKey)
* created_at

---

## SubCategory

* id
* name
* main_category (ForeignKey)
* user (ForeignKey)
* created_at

---

## Record

* id
* user (ForeignKey)
* transaction_type (income / expense)
* amount
* subcategory (ForeignKey)
* remarks
* created_at

---

# 🧭 System Flow

1. User registers and logs in
2. User is redirected to dashboard
3. User creates categories (main & sub)
4. User adds income/expense records
5. Data is stored in database
6. Dashboard calculates:

   * Total income
   * Total expense
   * Balance
7. User can filter records by type or category

---

# 🧠 System Architecture

```
User
 ├── Authentication (Login/Register)
 │
 ├── Dashboard
 │     ├── Income / Expense summary
 │     ├── Recent records
 │
 ├── Categories
 │     ├── MainCategory
 │     └── SubCategory
 │
 └── Records
       ├── Income / Expense entries
       └── linked to SubCategory
```

---

# 🔐 Security Features

* User authentication system
* Login required for all main pages
* Data isolation using `request.user`
* Each user only sees their own financial records

---

# 📊 Key Pages

| Page           | Description         |
| -------------- | ------------------- |
| `/register/`   | User registration   |
| `/login/`      | User login          |
| `/logout/`     | Logout              |
| `/dashboard/`  | Financial overview  |
| `/records/`    | Manage transactions |
| `/categories/` | Manage categories   |

---

# 👥 Team Roles

* **Backend Developer**: Django setup, models, business logic
* **Frontend Developer**: UI templates and design
* **Feature Developer**: Enhancements and system improvements

---

# 🔮 Future Improvements

* Add charts & analytics graphs
* Export reports (PDF/Excel)
* Budget planning system
* Better UI with Bootstrap or React
* Email notifications

---

# 📌 Notes

* Make sure virtual environment is activated before running project
* Do not use system-wide Python
* All user data is private and isolated per account

---

# 🏁 Project Status

✔ Authentication system completed
✔ Category system implemented
✔ Record tracking completed
✔ Dashboard analytics working
✔ Filtering system implemented

