This project implements a user authentication system using JWT (JSON Web Tokens) with FastAPI and MongoDB. It includes user CRUD operations, role-based access control (RBAC), and other essential features for building a secure and scalable user management system.

Features
JWT Authentication: Secure login, token issuance, and token validation.
User CRUD Operations: Create, Read, and Update users in a MongoDB database.
Role-Based Access Control (RBAC): Restrict access to certain endpoints based on user roles (e.g., admin, user).
Pydantic Models: User data validation and automated API documentation.
MongoDB Integration: Utilizes MongoDB for user data storage with the motor asynchronous driver.
Logging: Tracks API calls for better observability.
Secure Endpoints: Sensitive endpoints protected by JWT authentication and role validation.

add your .env file for database for running on server
