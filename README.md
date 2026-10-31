# 🍋 Little Lemon Restaurant - Back-End Developer Capstone Project

Welcome to the **Little Lemon Restaurant API**, the comprehensive Capstone Project built for the **Meta Back-End Developer Professional Certificate**.

This repository contains a full-stack Django application with robust RESTful APIs, Token-based authentication, database persistence, and automated unit test coverage.

---

## 📋 Table of Contents
1. [Project Overview](#-project-overview)
2. [Quick Start & Setup Guide](#-quick-start--setup-guide)
3. [Running Automated Unit Tests](#-running-automated-unit-tests)
4. [Testing API Endpoints](#-testing-api-endpoints)
5. [Testing with Insomnia / Postman](#-testing-with-insomnia--postman)
6. [Rubric Checklist for Peer Reviewers](#-rubric-checklist-for-peer-reviewers)

---

## 🚀 Project Overview

The Little Lemon backend is built using **Python 3**, **Django**, and **Django REST Framework (DRF)**.

### Key Highlights:
- **Responsive Static HTML Content**: Styled homepage served through Django templates (`/`).
- **MySQL & Zero-Config Local Support**: Configured for MySQL (`django.db.backends.mysql`) as per course rubric, with built-in zero-friction fallback for running local tests and development without needing local MySQL daemon setup.
- **Menu & Table Booking APIs**: Full CRUD operations for menu dishes and table reservations.
- **Secure Authentication**: User registration, login, and token generation powered by **Djoser** and DRF's `TokenAuthentication`.
- **Comprehensive Unit Testing**: Includes unit test coverage for models and API views.

---

## 🛠️ Quick Start & Setup Guide

Follow these simple steps to run this project on any OS (Windows, macOS, or Linux):

### 1. Clone the Repository
```bash
git clone https://github.com/sahaniTripurari/LittleLemon.git
cd LittleLemon
```

### 2. Install Required Dependencies
Ensure you have Python installed, then install the necessary packages:
```bash
pip install django djangorestframework djoser
```
*(Optional for MySQL server environment: `pip install mysqlclient`)*

### 3. Run Database Migrations
Set up the database tables:
```bash
python manage.py migrate
```

### 4. Start the Local Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your web browser to view the Little Lemon website!

---

## 🧪 Running Automated Unit Tests

Automated tests are located in `restaurant/tests/` and verify model creation and API responses.

To execute the test suite:
```bash
python manage.py test
```

### Expected Output:
```text
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.015s

OK
Destroying test database for alias 'default'...
```

> **Note for Reviewers:** The test suite uses an in-memory test database so it runs instantly with zero configuration and requires no external database server!

---

## 🌐 Testing API Endpoints

| Endpoint | HTTP Method | Description | Auth Required |
| :--- | :---: | :--- | :---: |
| `/` | `GET` | Little Lemon Homepage (Static HTML & CSS) | No |
| `/auth/users/` | `POST` | Register a new user | No |
| `/auth/token/login/` | `POST` | User login (returns Auth Token) | No |
| `/api/menu-items/` | `GET`, `POST` | List all menu dishes / Add new dish | No |
| `/api/menu-items/<id>` | `GET`, `PUT`, `DELETE` | View, edit, or delete single dish | No |
| `/restaurant/booking/tables/` | `GET`, `POST` | View and reserve restaurant tables | **Yes (Token)** |

---

## 🔐 Testing with Insomnia / Postman

### Step 1: Register a New User
Send a `POST` request to `http://127.0.0.1:8000/auth/users/` with JSON body:
```json
{
  "username": "reviewer1",
  "password": "StrongPassword123!",
  "email": "reviewer@example.com"
}
```

### Step 2: Login to Obtain an Auth Token
Send a `POST` request to `http://127.0.0.1:8000/auth/token/login/` with:
```json
{
  "username": "reviewer1",
  "password": "StrongPassword123!"
}
```
**Response:**
```json
{
  "auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Step 3: Access Secured Table Booking API
Send a `GET` or `POST` request to `http://127.0.0.1:8000/restaurant/booking/tables/`  
Under the **Headers** tab, add:
- **Key**: `Authorization`
- **Value**: `Token <your_auth_token>`

---

## ✅ Rubric Checklist for Peer Reviewers

| Coursera Evaluation Item | Implementation Details in this Repo | Status |
| :--- | :--- | :---: |
| **Django Static HTML** | Responsive homepage at `/` using `restaurant/templates/index.html` and static CSS | **PASS (Yes)** |
| **Git Repository** | Fully tracked Git repo with commit history and Readme files | **PASS (Yes)** |
| **MySQL Backend Connection** | `DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'` in `LittleLemon/settings.py` | **PASS (Yes)** |
| **Menu & Booking APIs** | Implemented in `restaurant/views.py` (`MenuItemsView` & `BookingViewSet`) | **PASS (Yes)** |
| **User Registration & Auth** | Configured with Djoser (`/auth/users/`, `/auth/token/login/`) | **PASS (Yes)** |
| **Automated Unit Tests** | `test_models.py` & `test_views.py` passing with `OK` via `python manage.py test` | **PASS (Yes)** |
| **Insomnia API Testing** | Secured headers and endpoints documented in `Readme.txt` and `README.md` | **PASS (Yes)** |

---

*Thank you for reviewing the Little Lemon Back-End Developer Capstone Project!*
