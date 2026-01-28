# 🎓 APU Café Management System

> A comprehensive Python-based role-based management system designed for café and educational institutions to efficiently manage users, courses, enrollment, and feedback across different organizational roles.

[![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Installation & Setup](#installation--setup)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [File Documentation](#file-documentation)
- [Database Schema](#database-schema)
- [Usage Guide](#usage-guide)
- [Role-Based Features](#role-based-features)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**APU Café Management System** is a multi-user, role-based application built entirely in Python. It provides a complete suite of tools for managing users, courses, enrollments, payments, and feedback in an educational café environment. The system uses a file-based JSON database for persistent data storage and implements a command-line interface (CLI) for user interaction.

### Key Highlights

- 🔐 **Role-Based Access Control** - 4 distinct user roles with specialized features
- 📊 **Multi-Module Management** - Complete course/module management system
- 💼 **User Management** - Registration, authentication, and profile management
- 📝 **Feedback System** - Collect suggestions and complaints from users
- 💾 **Persistent Storage** - JSON-based database with data integrity
- 🖥️ **Interactive CLI** - User-friendly command-line interfaces
- ✅ **Production-Ready** - Tested and debugged for stability

---

## ✨ Features

### Core Features

| Feature | Description |
|---------|-------------|
| **User Authentication** | Secure login system with role-based routing |
| **Role-Based Access** | 4 different roles with specialized permissions |
| **Profile Management** | Users can update their personal information |
| **Course Management** | Create, edit, and manage courses/modules |
| **Enrollment System** | Students can enroll in courses and manage modules |
| **Payment Tracking** | Track and manage student invoices and payments |
| **Feedback Collection** | Gather suggestions and complaints from users |
| **Request Management** | Students can submit and manage requests |
| **Data Persistence** | All data saved in JSON database files |

### Security Features

- User authentication with password protection
- Role-based access control (RBAC)
- Secure user data separation
- Password-protected operations

### Data Management Features

- User profile management
- Complete CRUD operations for courses
- Student enrollment tracking
- Invoice and payment management
- Feedback and complaint logging
- Request submission and tracking

---

## 🏗️ Project Architecture

### Architecture Pattern

The project follows a **layered architecture** pattern:

```
┌─────────────────────────────────┐
│     Display Layer (CLI)         │
│  (Role-Based Interfaces)        │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│       API/Business Layer        │
│  (User, Student, Lecturer, etc) │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│      Data Access Layer          │
│  (File I/O, JSON Operations)    │
└──────────────┬──────────────────┘
               │
┌──────────────┴──────────────────┐
│     Database Layer (JSON)       │
│  (Persistent Data Storage)      │
└─────────────────────────────────┘
```

### Module Communication Flow

```
main.py (Entry Point)
    ↓
    ├─→ user.py (Authentication)
    ├─→ display/{role}.py (CLI Interface)
    │   ↓
    │   └─→ api/{role}.py (Business Logic)
    │       ↓
    │       └─→ database/{role}s.json (Data)
    └─→ utils.py (Utility Functions)
```

---

## 💻 Installation & Setup

### Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package manager)
- **Windows, macOS, or Linux** (cross-platform compatible)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/apu-cafe-management.git
cd apu-cafe-management
```

### Step 2: Navigate to Project Directory

```bash
cd apu_cafe-main
```

### Step 3: Install Dependencies

This project uses only built-in Python libraries (no external dependencies required).

```bash
# No installation needed! The project uses standard library modules:
# - subprocess
# - json
# - os
# - uuid (for unique ID generation)
```

### Step 4: Verify Installation

```bash
# Test if Python is installed correctly
python --version

# List the project structure
ls -la  # macOS/Linux
dir     # Windows
```

### Step 5: Check Database Files

Ensure all database JSON files exist in the `database/` directory:

```bash
cd database
ls -la
```

You should see:
- `administrators.json`
- `lecturers.json`
- `trainers.json`
- `students.json`
- `modules.json`
- `feedbacks.json`

---

## 🚀 Quick Start

### Running the Application

```bash
cd apu_cafe-main
python main.py
```

### First-Time Setup

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Choose a role:**
   ```
   Enter as:
   1. Administrator
   2. Lecturer
   3. Trainer
   4. Student
   
   Enter choice: [1-4]
   ```

3. **Choose an action:**
   ```
   Action:
   1. Login
   2. Register
   
   Enter choice: [1-2]
   ```

4. **Register as a new user** (first time):
   ```
   Name: [Enter your name]
   Password: [Enter your password]
   ```

5. **Login** (subsequent times):
   ```
   Name: [Enter your name]
   Password: [Enter your password]
   ```

### Example Session

```bash
# Terminal Session
$ python main.py

Enter as:
1. Administrator
2. Lecturer
3. Trainer
4. Student

Enter choice: 4

Action:
1. Login
2. Register

Enter choice: 2
=== Register as Student ===
Name: John Doe
Password: secure123

Registration successful!

---

# Second Run - Login
$ python main.py

Enter as:
1. Administrator
2. Lecturer
3. Trainer
4. Student

Enter choice: 4

Action:
1. Login
2. Register

Enter choice: 1

Logging in as Student...
Name: John Doe
Password: secure123

Login successful!
[Student Dashboard appears]
```

---

## 📁 Project Structure

```
apu_cafe-main/
│
├── main.py                          # 🚀 Application Entry Point
├── utils.py                         # 🔧 Utility Functions
├── student.py                       # Legacy Student Operations
├── student display.py               # Legacy Student Display
│
├── api/                             # 📡 API & Business Logic Layer
│   ├── __init__.py
│   ├── user.py                      # User Authentication & Management
│   ├── student.py                   # Student Operations
│   ├── lecturer.py                  # Lecturer Operations
│   ├── trainer.py                   # Trainer Operations
│   ├── administrator.py             # Administrator Operations
│   ├── module.py                    # Course/Module Management
│   ├── feedback.py                  # Feedback Collection
│   └── __pycache__/
│
├── display/                         # 🖥️ CLI Interface Layer
│   ├── __init__.py
│   ├── student.py                   # Student Dashboard Interface
│   ├── lecturer.py                  # Lecturer Dashboard Interface
│   ├── trainer.py                   # Trainer Dashboard Interface
│   ├── administrator.py             # Administrator Dashboard Interface
│   └── __pycache__/
│
├── database/                        # 💾 Data Storage Layer
│   ├── administrators.json          # Admin user data
│   ├── lecturers.json              # Lecturer profiles
│   ├── trainers.json               # Trainer profiles
│   ├── students.json               # Student profiles & records
│   ├── modules.json                # Course/Module definitions
│   └── feedbacks.json              # User feedback & complaints
│
├── __pycache__/                     # Python cache files
├── README.md                        # 📖 This File
├── BUG_ANALYSIS.md                 # 🐛 Bug Documentation
├── FIXES_SUMMARY.md                # ✅ Fixes Applied
├── REQUIREMENTS_VALIDATION_REPORT.md # 📋 Requirements Checklist
└── .gitignore                       # Git ignore rules
```

---

## 📚 File Documentation

### Entry Point

#### `main.py` (63 lines)
**Purpose:** Application entry point and role routing

**Key Functionality:**
- Displays role selection menu (Administrator, Lecturer, Trainer, Student)
- Handles user authentication (login/registration)
- Routes users to their role-specific dashboard
- Manages subprocess execution for display modules

**Main Functions:**
- `handle_login()` - Authenticates user credentials
- `handle_register()` - Creates new user accounts

**Example Usage:**
```python
# When login is successful, routes to display module:
subprocess.run(["python", "-m", f"display.{type}", status["id"]], cwd=script_dir)
```

---

### Utility Module

#### `utils.py` (11 lines)
**Purpose:** Shared utility functions across the application

**Functions:**
- `select(message, items)` - Interactive menu selection helper
  - Displays a numbered list of items
  - Validates user input
  - Returns selected item

**Example:**
```python
role = select("Choose your role:", ["Student", "Lecturer", "Admin"])
```

---

### API Layer (Business Logic)

#### `api/user.py`
**Purpose:** Central authentication and user management hub

**Key Functions:**
- `check(type, username, password)` - Authenticates user credentials
- `load_data(type)` - Loads user data from JSON
- `set(type, id, key, value)` - Updates user data
- `get(type, username)` - Retrieves user by username
- `register(type, name, password)` - Creates new user account

**Data Flow:**
```python
user.check("student", "john", "pass123")
→ Returns: {"exists": True, "match": True, "id": "uuid-123"}
```

---

#### `api/student.py`
**Purpose:** Student-specific operations and management

**Key Functions:**
- `change_password(student_id, new_password)` - Update password
- `change_contact(student_id, new_contact)` - Update contact info
- `change_address(student_id, new_address)` - Update address
- `add_module(student_id, module_id)` - Enroll in a course
- `pay_invoice(student_id, invoice_id)` - Record payment
- `add_request(student_id, request_data)` - Submit request
- `delete_request(student_id, request_id)` - Cancel request
- `delete(student_id)` - Delete student account

**Features:**
- Personal information management
- Course enrollment tracking
- Invoice and payment management
- Request submission system

---

#### `api/lecturer.py`
**Purpose:** Lecturer profile and information management

**Key Functions:**
- `get_all()` - Retrieve all lecturers
- `get(lecturer_id)` - Get specific lecturer
- `change_name(lecturer_id, new_name)` - Update name
- `change_qualification(lecturer_id, new_qualification)` - Update qualifications
- `change_department(lecturer_id, new_department)` - Update department

**Data Managed:**
- Lecturer profiles
- Qualifications and certifications
- Department assignments

---

#### `api/trainer.py`
**Purpose:** Trainer management and feedback operations

**Key Functions:**
- `get_all()` - Retrieve all trainers
- `get(trainer_id)` - Get specific trainer
- `add_feedback(trainer_id, feedback_data)` - Collect trainer feedback

**Features:**
- Trainer profile management
- Feedback collection
- Performance tracking

---

#### `api/administrator.py`
**Purpose:** Administrator authentication and system oversight

**Key Functions:**
- `check(name, password)` - Admin authentication
- `get_all()` - Retrieve all admins

**Responsibilities:**
- System authentication
- Administrative access control

---

#### `api/module.py`
**Purpose:** Complete course/module management system

**Key Functions:**
- `create(name, lecturer_id, language, level)` - Create new module
- `add_schedule(module_id, schedule_data)` - Add course schedule
- `remove_schedule(module_id, schedule_id)` - Remove schedule
- `edit_schedule(module_id, schedule_id, new_data)` - Edit schedule
- `add_student(module_id, student_id)` - Enroll student
- `pay_student_invoice(module_id, student_id, amount)` - Process payment
- `remove_student(module_id, student_id)` - Remove from course
- `delete(module_id)` - Delete module
- `get_filtered_modules(language, level)` - Search/filter modules

**Module Properties:**
```json
{
  "id": "uuid",
  "name": "Module Name",
  "lecturer_id": "uuid",
  "language": "English",
  "level": "Intermediate",
  "schedules": [],
  "students": [],
  "invoices": {}
}
```

---

#### `api/feedback.py`
**Purpose:** Feedback and complaint collection system

**Key Functions:**
- `add_suggestion(name, suggestion)` - Record suggestions
- `add_complaint(name, complaint)` - Record complaints
- `get_all()` - Retrieve all feedback
- `get_complaints()` - Get all complaints
- `get_suggestions()` - Get all suggestions

**Feedback Types:**
- Suggestions (improvements, ideas)
- Complaints (issues, problems)

---

### Display Layer (CLI Interfaces)

#### `display/student.py`
**Purpose:** Student dashboard and interactive interface

**Features Provided:**
- View profile
- Update password, contact, address
- Enroll in modules
- View enrolled modules
- View and manage invoices
- Submit and manage requests
- Access feedback system

**Interface:**
```
=== Student Dashboard ===
1. View Profile
2. Update Password
3. Update Contact
4. Update Address
5. Add Module
6. View Modules
7. Pay Invoice
8. Add Request
9. View Requests
10. Exit
```

---

#### `display/lecturer.py`
**Purpose:** Lecturer dashboard and operations

**Features Provided:**
- View profile
- Update name, qualifications, department
- View assigned modules
- View enrolled students
- Manage course schedules

**Interface:**
```
=== Lecturer Dashboard ===
1. View Profile
2. Update Name
3. Update Qualifications
4. Update Department
5. View Modules
6. View Students
7. Exit
```

---

#### `display/trainer.py`
**Purpose:** Trainer dashboard and feedback management

**Features Provided:**
- View trainer profile
- Submit feedback
- View all feedbacks
- Performance tracking

**Interface:**
```
=== Trainer Dashboard ===
1. View Profile
2. Submit Feedback
3. View Feedbacks
4. Exit
```

---

#### `display/administrator.py`
**Purpose:** Administrator dashboard with system-wide controls

**Features Provided:**
- View all users by role
- View all modules
- View all feedback and complaints
- System statistics
- User management

**Interface:**
```
=== Administrator Dashboard ===
1. View All Users
2. View All Modules
3. View All Feedback
4. View Complaints
5. View Suggestions
6. Exit
```

---

### Database Files

#### `database/administrators.json`
**Purpose:** Administrator account storage

**Structure:**
```json
[
  {
    "id": "unique-uuid",
    "name": "Admin Name",
    "password": "plain-text-password"
  }
]
```

---

#### `database/students.json`
**Purpose:** Student profiles and academic records

**Structure:**
```json
[
  {
    "id": "unique-uuid",
    "name": "Student Name",
    "password": "plain-text-password",
    "contact": "+1234567890",
    "address": "123 Main St",
    "modules": ["module-uuid-1", "module-uuid-2"],
    "requests": [
      {
        "id": "request-uuid",
        "type": "support",
        "message": "Request text"
      }
    ],
    "invoices": {
      "module-uuid": 500.00
    }
  }
]
```

---

#### `database/lecturers.json`
**Purpose:** Lecturer profiles and information

**Structure:**
```json
[
  {
    "id": "unique-uuid",
    "name": "Lecturer Name",
    "password": "plain-text-password",
    "qualifications": "M.Sc, B.Sc",
    "department": "Computer Science",
    "modules": ["module-uuid-1"]
  }
]
```

---

#### `database/trainers.json`
**Purpose:** Trainer profiles

**Structure:**
```json
[
  {
    "id": "unique-uuid",
    "name": "Trainer Name",
    "password": "plain-text-password",
    "specialization": "Web Development"
  }
]
```

---

#### `database/modules.json`
**Purpose:** Course and module definitions

**Structure:**
```json
[
  {
    "id": "unique-uuid",
    "name": "Python Programming",
    "lecturer_id": "lecturer-uuid",
    "language": "English",
    "level": "Beginner",
    "schedules": [
      {
        "id": "schedule-uuid",
        "day": "Monday",
        "time": "10:00 AM",
        "room": "101"
      }
    ],
    "students": ["student-uuid-1", "student-uuid-2"],
    "invoices": {
      "student-uuid-1": 500.00
    }
  }
]
```

---

#### `database/feedbacks.json`
**Purpose:** User feedback, suggestions, and complaints

**Structure:**
```json
[
  {
    "id": "unique-uuid",
    "name": "User Name",
    "type": "suggestion|complaint",
    "message": "Feedback content",
    "timestamp": "2026-01-28T10:30:00"
  }
]
```

---

## 🔐 Database Schema

### User Entities

```
┌─────────────────────────────┐
│      Administrator          │
├─────────────────────────────┤
│ id (UUID)                   │
│ name (String)               │
│ password (String)           │
└─────────────────────────────┘

┌─────────────────────────────┐
│       Student               │
├─────────────────────────────┤
│ id (UUID)                   │
│ name (String)               │
│ password (String)           │
│ contact (String)            │
│ address (String)            │
│ modules (Array<UUID>)       │
│ requests (Array<Object>)    │
│ invoices (Object<UUID>)     │
└─────────────────────────────┘

┌─────────────────────────────┐
│       Lecturer              │
├─────────────────────────────┤
│ id (UUID)                   │
│ name (String)               │
│ password (String)           │
│ qualifications (String)     │
│ department (String)         │
│ modules (Array<UUID>)       │
└─────────────────────────────┘

┌─────────────────────────────┐
│       Trainer               │
├─────────────────────────────┤
│ id (UUID)                   │
│ name (String)               │
│ password (String)           │
│ specialization (String)     │
└─────────────────────────────┘
```

### Resource Entities

```
┌─────────────────────────────┐
│       Module                │
├─────────────────────────────┤
│ id (UUID)                   │
│ name (String)               │
│ lecturer_id (UUID)          │
│ language (String)           │
│ level (String)              │
│ schedules (Array<Object>)   │
│ students (Array<UUID>)      │
│ invoices (Object<UUID>)     │
└─────────────────────────────┘

┌─────────────────────────────┐
│       Feedback              │
├─────────────────────────────┤
│ id (UUID)                   │
│ name (String)               │
│ type (String)               │
│ message (String)            │
│ timestamp (ISO-8601)        │
└─────────────────────────────┘
```

---

## 📖 Usage Guide

### Scenario 1: Student Registration and Course Enrollment

```bash
# Step 1: Run the application
python main.py

# Step 2: Select Student role
# Choose: 1. Administrator 2. Lecturer 3. Trainer 4. Student
# Enter: 4

# Step 3: Select Register
# Choose: 1. Login 2. Register
# Enter: 2

# Step 4: Enter student details
# Name: Alice Johnson
# Password: secure_pass

# Step 5: In Student Dashboard
# Choose: 5. Add Module
# Enter: Select a module from the list

# Step 6: View enrolled modules
# Choose: 6. View Modules
# Displays: All modules you're enrolled in
```

---

### Scenario 2: Lecturer Managing Courses

```bash
# Step 1: Run application and login as Lecturer
python main.py
# Select: 2 (Lecturer)
# Action: 1 (Login)

# Step 2: Access Lecturer Dashboard
# Credentials: Existing lecturer account

# Step 3: View assigned modules
# Choose: 5. View Modules
# Displays: All modules assigned to this lecturer

# Step 4: View enrolled students
# Choose: 6. View Students
# Displays: Students in assigned modules
```

---

### Scenario 3: Administrator System Oversight

```bash
# Step 1: Login as Administrator
python main.py
# Select: 1 (Administrator)
# Action: 1 (Login)

# Step 2: Access Admin Dashboard
# Choose: 1. View All Users
# Displays: All users by role

# Step 3: View all feedback
# Choose: 3. View All Feedback
# Displays: All user suggestions and complaints

# Step 4: View system statistics
# Choose: 5. View Suggestions
# Or: 4. View Complaints
```

---

## 🎭 Role-Based Features

### Administrator

| Feature | Permission |
|---------|-----------|
| View All Users | ✅ |
| Manage Roles | ✅ |
| View System Statistics | ✅ |
| Access Feedback | ✅ |
| Manage Modules | ✅ |
| System Configuration | ✅ |

### Lecturer

| Feature | Permission |
|---------|-----------|
| View Profile | ✅ |
| Update Qualifications | ✅ |
| Manage Modules | ✅ |
| View Students | ✅ |
| Manage Schedules | ✅ |
| Submit Feedback | ✅ |

### Trainer

| Feature | Permission |
|---------|-----------|
| View Profile | ✅ |
| Submit Feedback | ✅ |
| View Feedbacks | ✅ |
| Performance Tracking | ✅ |

### Student

| Feature | Permission |
|---------|-----------|
| View Profile | ✅ |
| Update Password | ✅ |
| Update Contact Info | ✅ |
| Update Address | ✅ |
| Enroll in Courses | ✅ |
| View Invoices | ✅ |
| Pay Invoices | ✅ |
| Submit Requests | ✅ |
| Submit Feedback | ✅ |

---

## ⚙️ Configuration

### User Configuration

Users can customize their profiles:

```python
# Update student information
api.student.change_password(student_id, "newpassword")
api.student.change_contact(student_id, "+1-555-0123")
api.student.change_address(student_id, "456 Oak Ave, City")

# Update lecturer information
api.lecturer.change_name(lecturer_id, "Dr. New Name")
api.lecturer.change_qualification(lecturer_id, "Ph.D")
```

### Module Configuration

```python
# Create a new module
api.module.create(
    name="Advanced Python",
    lecturer_id="lecturer-uuid",
    language="English",
    level="Advanced"
)

# Add course schedule
api.module.add_schedule(
    module_id="module-uuid",
    schedule_data={
        "day": "Tuesday",
        "time": "2:00 PM",
        "room": "201"
    }
)
```

---

## 🔍 Troubleshooting

### Issue: FileNotFoundError: 'database/students.json' not found

**Solution:**
1. Ensure you're in the correct directory: `cd apu_cafe-main`
2. Check that all database JSON files exist: `ls database/`
3. If missing, they will be created on first run

### Issue: ModuleNotFoundError: No module named 'display'

**Solution:**
1. Run from the correct directory where `main.py` is located
2. Use the full path: `python apu_cafe-main/main.py`
3. Ensure `__init__.py` files exist in `api/` and `display/` directories

### Issue: Invalid user input errors

**Solution:**
1. Enter numeric choices when prompted (1, 2, 3, etc.)
2. Enter valid usernames and passwords
3. Follow on-screen prompts carefully

### Issue: Login fails even with correct credentials

**Solution:**
1. Check that the user was properly registered
2. Ensure database files are not corrupted
3. Verify password is case-sensitive
4. Try registering again with a new account

### Issue: Application crashes unexpectedly

**Solution:**
1. Check Python version: `python --version` (requires 3.7+)
2. Verify all database files are present and readable
3. Check for file permission issues
4. Review error messages in terminal output

---

## 🐛 Known Issues & Fixes

### Fixed Issues

✅ **Loop Variable Shadowing** - Fixed in `api/student.py`
- Function parameters no longer shadow iterator variables

✅ **FileNotFoundError** - Fixed with absolute path handling
- All file operations now use absolute paths

✅ **Resource Leaks** - Fixed with context managers
- All file operations use `with` statements

✅ **Parameter Typos** - Fixed in `api/lecturer.py` and `api/module.py`
- All parameter names are now correct

---

## 📦 Dependencies

**No External Dependencies Required!**

The project uses only Python Standard Library modules:

```python
import subprocess  # Process management
import json        # Data serialization
import os          # File path operations
import uuid        # Unique ID generation
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/apu-cafe-management.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** and test thoroughly

4. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: description of changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** with detailed description

### Contribution Guidelines

- Follow the existing code style
- Add comments for complex logic
- Test all changes thoroughly
- Update documentation as needed
- Keep commits focused and atomic

---

## 📋 Future Enhancements

Potential features for future versions:

- [ ] **Database Migration** - Migrate from JSON to SQLite
- [ ] **Password Hashing** - Implement bcrypt for security
- [ ] **User Sessions** - Add session management
- [ ] **Logging System** - Implement audit logging
- [ ] **Email Notifications** - Send notifications to users
- [ ] **Web API** - REST API for web clients
- [ ] **GUI Interface** - Desktop GUI using tkinter/PyQt
- [ ] **Data Export** - Export reports to CSV/PDF
- [ ] **Backup System** - Automated database backup
- [ ] **Multi-language Support** - Internationalization

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Copyright (c) 2026 APU Café Management System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 📧 Support & Contact

**Project Maintainer:** Faiyad Mahabub Tasin  
**Email:** faiyaadtasin121@gmail.com  
**GitHub:** https://github.com/faiyaadmahabub-hash

For issues, questions, or suggestions:
- Open an Issue on GitHub
- Check existing documentation
- Review troubleshooting section

---

## 🎓 Educational Value

This project demonstrates:

- ✅ Object-oriented programming principles
- ✅ Role-based access control (RBAC)
- ✅ Layered architecture design
- ✅ File I/O and data persistence
- ✅ Interactive CLI development
- ✅ Code organization and modularity
- ✅ Error handling best practices
- ✅ Data validation and integrity
- ✅ Professional code documentation

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Files | 15+ |
| Lines of Code | 1500+ |
| Core Modules | 7 |
| Display Interfaces | 4 |
| Database Files | 6 |
| User Roles | 4 |
| Key Features | 20+ |
| Documentation Files | 4 |

---

## 🎉 Credits

- **Developer:** Faiyad Mahabub Tasin
- **Institution:** Asia Pacific University
- **Course:** Python Programming
- **Version:** 1.0
- **Last Updated:** January 28, 2026

---

## 📌 Quick Reference

### Common Commands

```bash
# Run the application
python main.py

# Check Python version
python --version

# List project structure
tree apu_cafe-main/

# View a specific file
cat api/student.py

# Check database files
ls database/

# Run tests (if available)
python -m pytest tests/
```

### Quick Navigation

- 📖 **Documentation:** See [README.md](README.md)


---

**Happy Coding! 🚀**

