FastAPI DataFrames Project

This repository contains a FastAPI application with two main features: managing users and products. The application interacts with a PostgreSQL database and provides RESTful APIs for these entities.

Table of Contents

Features

Requirements

Installation

Usage

Project Structure

API Endpoints

License

Features

CRUD operations for Users and Products.

PostgreSQL integration using SQLAlchemy.

Modular and scalable structure with routers.

Easy-to-use dependency injection for database sessions.

Requirements

To run this project, ensure you have the following installed:

Python 3.8+

PostgreSQL

Virtual environment tool (recommended)

Installation

Follow these steps to set up the project:

Clone the repository:

git clone https://github.com/your-username/fastapi-dataframes.git
cd fastapi-dataframes

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate   # For Windows

Install dependencies:

pip install -r requirements.txt

Configure the database:

Update the DATABASE_URL in app/database.py with your PostgreSQL credentials:

DATABASE_URL = "postgresql://username:password@localhost:5432/fastapi_db"

Run migrations:

Create tables in the database:

python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"

Start the application:

Run the application using Uvicorn:

uvicorn app.main:app --reload

The app will be available at http://127.0.0.1:8000.

Usage

Access API documentation:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Test endpoints:

Use the provided documentation to test endpoints for users and products.

Project Structure

fastapi-dataframes/
├── app/
│   ├── __init__.py
│   ├── database.py         # Database configuration
│   ├── models.py           # SQLAlchemy models
│   ├── routers/            # Routers for API endpoints
│   │   ├── __init__.py
│   │   ├── users.py        # User-related endpoints
│   │   └── products.py     # Product-related endpoints
│   └── main.py             # Application entry point
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

API Endpoints

Users

GET /api/users: Retrieve all users

POST /api/users: Create a new user (extend functionality as needed)

Products

GET /api/products: Retrieve all products

POST /api/products: Create a new product (extend functionality as needed)