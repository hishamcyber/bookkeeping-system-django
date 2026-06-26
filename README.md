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
* user (ForeignKey → User)
* created_at

---

## SubCategory

* id
* name
* main_category (ForeignKey → MainCategory)
* user (ForeignKey → User)
* created_at

---

## Record

* id
* user (ForeignKey → User)
* main_category (ForeignKey → MainCategory)
* subcategory (ForeignKey → SubCategory, optional)
* transaction_type (income / expense)
* amount
* remarks (optional)
* created_at

---

# 🧭 System Flow

1. User registers → default categories are auto-created for their account
2. User logs in and is redirected to dashboard
3. Dashboard shows total income, total expense, and current balance
4. User can add custom Main and Sub categories
5. User can delete any category they created
6. User adds income/expense records by selecting:
   - Main Category (dropdown)
   - Sub Category (optional, auto-updates based on main category via AJAX)
   - Transaction type (income/expense)
   - Amount
   - Remarks (optional)
7. Records are saved and reflected in dashboard stats

---

# 🧠 System Architecture

```
User
 ├── Authentication (Login/Register)
│     └── Default categories auto-created on register
│
├── Dashboard
│     ├── Total Income / Expense / Balance cards
│     ├── Recent categories quick access
│     ├── Recent records (last 5)
│     └── Navigation to Records and Categories
│
├── Categories
│     ├── MainCategory (add / delete)
│     └── SubCategory (add / delete, linked to MainCategory)
│
└── Records
├── Income / Expense entries
├── Linked to MainCategory and SubCategory
└── AJAX subcategory filtering by selected main category

---

# 🔐 Security Features

* User authentication required for all main pages (`@login_required`)
* Data isolation using `request.user` on all queries
* Each user only sees their own categories and records
* Category deletion protected — users can only delete their own categories

---

# 📊 Key Pages

| Page                           | Description                        |
| ------------------------------ | ---------------------------------- |
| `/register/`                   | User registration                  |
| `/login/`                      | User login                         |
| `/logout/`                     | Logout                             |
| `/dashboard/`                  | Financial overview                 |
| `/records/`                    | View all transaction records       |
| `/records/add/`                | Add new income/expense record      |
| `/records/get-subcategories/`  | AJAX endpoint for subcategory data |
| `/categories/`                 | View, add, and delete categories   |
| `/categories/add/`             | Add new main or sub category       |
| `/categories/delete/<type>/<id>/` | Delete a category               |

---

# 👥 Team Roles

* **Backend Developer (Orgil)**: Category CRUD logic, record form logic, AJAX subcategory filtering, default category signal, data isolation
* **Frontend Developer (Noura)**: UI templates, Three.js backgrounds, cyberpunk theme design
* **Project Lead (Hisham)**: Django setup, models, authentication, dashboard, project architecture

---

# 🔮 Future Improvements

* Add charts & analytics graphs
* Export reports (PDF/Excel)
* Budget planning system
* Email notifications
* Record editing and deletion
* Filter records by category or date range

---

# 📌 Notes

* Always activate virtual environment before running the project
* Do not use system-wide Python
* On Windows PowerShell, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` if activation fails
* All user data is private and isolated per account
* Default categories are automatically created for every new user on registration

---

# 🏁 Project Status

✔ Authentication system completed  
✔ Default category auto-creation on registration  
✔ Category system implemented (add / delete main & sub)  
✔ Record tracking completed (with main & sub category selection)  
✔ AJAX subcategory filtering implemented  
✔ Dashboard analytics working  
✔ User data isolation implemented
