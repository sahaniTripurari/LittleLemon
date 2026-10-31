Little Lemon Restaurant - Back-End Developer Capstone Project

API Paths for Peer Reviewers to Test:
1. Static HTML Homepage:
   GET http://127.0.0.1:8000/

2. User Registration (Djoser):
   POST http://127.0.0.1:8000/auth/users/

3. Token Login (Djoser TokenAuthentication):
   POST http://127.0.0.1:8000/auth/token/login/

4. Menu Items API (List & Create):
   GET  http://127.0.0.1:8000/api/menu-items/
   POST http://127.0.0.1:8000/api/menu-items/

5. Single Menu Item API (Retrieve, Update, Delete):
   GET    http://127.0.0.1:8000/api/menu-items/<id>
   PUT    http://127.0.0.1:8000/api/menu-items/<id>
   DELETE http://127.0.0.1:8000/api/menu-items/<id>

6. Table Booking API (Secured with Token Authentication):
   GET  http://127.0.0.1:8000/restaurant/booking/tables/
   POST http://127.0.0.1:8000/restaurant/booking/tables/

Testing with Insomnia / Postman:
- Pass Header 'Authorization: Token <token_key>' to access the /restaurant/booking/tables/ endpoint.
