# Little Lemon Restaurant - Back-End Developer Capstone Project

This repository contains the completed Capstone Project for the **Meta Back-End Developer Professional Certificate**.

## Project Overview
The Little Lemon API is built with **Django** and **Django REST Framework (DRF)**. It provides robust API endpoints to manage restaurant bookings, browse menu items, and authenticate users with Token-based authentication.

---

## Features
- **Static HTML Content**: Serves responsive static web pages using Django templates and static files.
- **MySQL Database Connection**: Configured for MySQL database connectivity.
- **Menu & Table Booking APIs**: Full CRUD capabilities for menu items and table reservations.
- **User Authentication**: User registration and login powered by Djoser and DRF's `TokenAuthentication`.
- **Unit Testing**: Automated model and view test coverage.

---

## API Endpoints for Peer Review

| Endpoint | Method | Description | Auth Required |
| :--- | :---: | :--- | :---: |
| `/` | `GET` | Home / Static HTML page | No |
| `/auth/users/` | `POST` | User registration | No |
| `/auth/token/login/` | `POST` | User login (returns auth token) | No |
| `/api/menu-items/` | `GET`, `POST` | List and create menu items | No |
| `/api/menu-items/<id>` | `GET`, `PUT`, `DELETE` | Retrieve, update, delete menu item | No |
| `/restaurant/booking/tables/` | `GET`, `POST` | Manage table bookings | **Yes (Token)** |

---

## Testing in Insomnia / Postman
To test secured endpoints like `/restaurant/booking/tables/`:
1. Obtain an auth token by sending a `POST` request to `/auth/token/login/` with `username` and `password`.
2. Copy the `auth_token` received.
3. In the request headers for `/restaurant/booking/tables/`, add:
   - **Key**: `Authorization`
   - **Value**: `Token <your_auth_token>`

---

## Running the Unit Tests
Execute the automated test suite with:
```bash
python manage.py test
```
