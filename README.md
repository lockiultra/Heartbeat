# Medical Management System API

This project is a backend API for managing medical data, including patients and doctors. It is built using FastAPI, SQLAlchemy, and Pydantic, and is designed to be asynchronous for better performance.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Schemas](#schemas)
- [Repository Pattern](#repository-pattern)
- [Authentication](#authentication)
- [Database](#database)
- [Settings](#settings)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- **CRUD Operations**: Create, Read, Update, and Delete operations for patients and doctors.
- **Asynchronous**: Built using FastAPI and SQLAlchemy for asynchronous database operations.
- **Repository Pattern**: Clean separation of concerns with a repository pattern for database interactions.
- **Pydantic Schemas**: Data validation and serialization using Pydantic models.
- **Authentication**: Password hashing using `bcrypt`.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/medical-management-system.git
   cd medical-management-system
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory with the following content:
   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
   TEST_DATABASE_URL=postgresql+asyncpg://user:password@localhost/testdb
   ALGORITHM=HS256
   ```

5. **Run the application**:
   ```bash
   uvicorn backend.api.main:app --reload
   ```

## Usage

The API will be available at `http://127.0.0.1:8000/`. You can interact with the API using tools like `curl`, `Postman`, or directly through the Swagger UI at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Patients
- **GET** `/patient/` - Get all patients.
- **GET** `/patient/{id}` - Get a patient by ID.
- **POST** `/patient/` - Create a new patient.
- **PUT** `/patient/` - Update a patient.
- **DELETE** `/patient/{id}` - Delete a patient.

### Doctors
- **GET** `/doctor/` - Get all doctors.
- **GET** `/doctor/{id}` - Get a doctor by ID.
- **POST** `/doctor/` - Create a new doctor.
- **PUT** `/doctor/` - Update a doctor.
- **DELETE** `/doctor/` - Delete a doctor.

## Models

### User
- **id**: `int` - Primary key.
- **first_name**: `str` - First name of the user.
- **last_name**: `str` - Last name of the user.
- **middle_name**: `str` - Middle name of the user (optional).
- **username**: `str` - Unique username.
- **password**: `str` - Hashed password.

### Patient
- Inherits from `User`.
- **insurance**: `str` - Insurance information.

### Doctor
- Inherits from `User`.
- **speciality**: `DOCTOR_SPEC` - Speciality of the doctor.

### Appointment
- **TODO**: Define appointment model.

## Schemas

### User
- **UserBase**: Base schema for user.
- **UserGet**: Schema for retrieving user data.
- **UserCreate**: Schema for creating a new user.
- **UserUpdate**: Schema for updating user data.
- **UserDelete**: Schema for deleting a user.

### Patient
- **PatientBase**: Base schema for patient.
- **PatientGet**: Schema for retrieving patient data.
- **PatientCreate**: Schema for creating a new patient.
- **PatientUpdate**: Schema for updating patient data.
- **PatientDelete**: Schema for deleting a patient.

### Doctor
- **DoctorBase**: Base schema for doctor.
- **DoctorGet**: Schema for retrieving doctor data.
- **DoctorCreate**: Schema for creating a new doctor.
- **DoctorUpdate**: Schema for updating doctor data.
- **DoctorDelete**: Schema for deleting a doctor.

## Repository Pattern

The repository pattern is used to abstract the database layer. Each entity (e.g., Patient, Doctor) has its own repository class that inherits from `BaseRepository`.

### BaseRepository
- **get_all**: Retrieve all records.
- **get_by_id**: Retrieve a record by ID.
- **create**: Create a new record.
- **update**: Update an existing record.
- **delete**: Delete a record.

### PatientRepository
- Inherits from `BaseRepository`.
- Implements CRUD operations for patients.

### DoctorRepository
- Inherits from `BaseRepository`.
- Implements CRUD operations for doctors.

## Authentication

Password hashing is done using `bcrypt` via the `passlib` library. The `get_password_hash` function is used to hash passwords before storing them in the database.

## Database

The database is managed using SQLAlchemy with an asynchronous engine. The `create_tables` function is used to create all necessary tables in the database.

## Settings

The `Settings` class is used to manage environment variables, such as database URLs and algorithm settings. These settings are loaded from a `.env` file.

## Testing

The `backend/tests/` directory is reserved for unit and integration tests. Currently, no tests are implemented.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.