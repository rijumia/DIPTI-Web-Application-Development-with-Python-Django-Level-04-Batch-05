# 🏢 Django Office Management System

A web-based Office Management System built using Django that manages Employees, Departments, and Leave Requests. The system supports two user roles: **Admin** and **Employee**.

---

## 🚀 Features

### 🔐 Authentication
- Secure Login and Logout system using Django Authentication
- User roles:
  - **Admin**: Full control of the system
  - **Employee**: Limited access to own profile and leave requests

---

### 👨‍💼 Employee Management
**Admin Capabilities:**
- Add new employees
- View all employees
- (Planned) Edit and delete employee profiles

**Employee Capabilities:**
- View and edit own profile

**Fields:**
- Full Name
- Email
- Phone
- Department (ForeignKey)
- Position
- Date of Joining
- Profile Picture

---

### 🏬 Department Management
**Admin Capabilities:**
- Create departments
- View list of departments
- (Planned) Edit and delete departments
- (Planned) View employees by department

**Fields:**
- Name
- Description

---

### 📝 Leave Management
**Employee Capabilities:**
- Apply for leave
- View own leave history

**Admin Capabilities:**
- View all leave requests
- Approve or reject leave requests

**Fields:**
- Employee (ForeignKey)
- Leave Type
- From Date
- To Date
- Reason
- Status (Pending, Approved, Rejected)

---

### 📊 Dashboards

#### Admin Dashboard
- Total employees
- Total departments
- Total pending leave requests

#### Employee Dashboard
- Welcome message
- Profile summary
- Leave summary

---

## 🛠️ Technologies Used
- Python 3.12+
- Django 5.2.4
- SQLite3 (default database)
- Bootstrap (for UI)
- HTML5, CSS3

---

## 🏁 Getting Started

### 1. Clone the project
```bash
git clone https://github.com/yourusername/office-management-system.git
cd office-management-system
