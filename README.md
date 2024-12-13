# Final-Project-In-ACP

# Passenger and Bus Management Application

This repository contains two Python applications designed for managing passenger information and bus assignments using Tkinter for the GUI and MySQL for the database.

---

## Overview

### Applications:
1. **PassengerApp**: Allows passengers to log in, sign up, and manage their information.
2. **BusManagementApp**: Provides functionality for managing bus assignments and passenger details, designed for tour guides and administrators.

### Features:
- User authentication (Log In/Sign Up)
- Passenger details submission and management
- Bus assignment and passenger tracking
- Database-driven data storage and retrieval

---

## Prerequisites

### Required Software:
- Python (3.6 or higher)
- MySQL Database
- Required Python Libraries:
  - `tkinter`
  - `mysql-connector-python`
  - `Pillow`

### Database Setup:
1. Ensure MySQL is installed and running.
2. Create a database named `bus_management1`.
3. Create the following tables:
   - `user`: For storing user credentials.
   - `passengerinfo`: For storing passenger details.
   - `bus1`: For managing bus assignments.
   - `adminuser`: For tour guide/admin credentials.



---

## Usage

### PassengerApp
1. Run `PassengerApp.py`.
2. Features:
   - **Log In**: Authenticate with username and password.
   - **Sign Up**: Register a new account.
   - **Passenger Form**: Submit details like name, contact, and assign a bus ID and seat number.

### BusManagementApp
1. Run `BusManagementApp.py`.
2. Features:
   - **Tour Guide Log In**: Authenticate as a tour guide.
   - **Search Passengers**: Retrieve passenger details based on bus ID.
   - **OnBoard/OffBoard**: Update the attendance of passengers.
   - **Delete Passenger**: Remove passenger details from the database.

---

## Configuration

Update the following constants in both scripts to match your MySQL setup:
```python
DB_HOST = '127.0.0.1'
DB_NAME = 'bus_management1'
DB_USER = 'root'
DB_PASSWORD = 'bancoro6'
```

---

## Project Structure
- `PassengerApp.py`: Passenger management application.
- `BusManagementApp.py`: Bus and tour guide management application.

---

## Screenshots
1. **Login Screen**: User-friendly interface for authentication.
2. **Passenger Form**: Form for inputting passenger details.
3. **Bus Management**: Admin view for managing passengers and buses.

---

## Authors
- Developed by [Niño Rico C. Bancoro, Mat Jannus Deguzman, John MArk Jebulan, Lawrence Villalobos].

---

## Contact
For issues or inquiries, please contact:
- Email: laveratours2006@gmail.com
- Phone: 09178913571 / 09171555358 / 09665272931.
