# Day 88 - Cafe and Wifi Website

## Goal
Build a website that lists cafes with wifi and power for remote working.

## Overview

The Cafe and Wifi Website is a web application built using Flask that helps users find cafes suitable for remote working. It allows users to view, search, add, and delete cafes that offer wifi and power sockets. The application also includes a feature to display a random cafe from the database.

## Features

- **View Cafes**: See a list of all cafes with details such as location, seats, wifi availability, and coffee price.
- **Search Cafes**: Search for cafes by location.
- **Add New Cafe**: Submit a form to add a new cafe to the database.
- **Delete Cafe**: Remove a cafe from the database.
- **Random Cafe**: Display a randomly selected cafe from the database.

Demo:

![Demo](./Coffee%20and%20wifi.gif)

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Flask-SQLAlchemy**: An SQLAlchemy integration for Flask.
- **Flask-WTF**: An extension that simplifies form handling.
- **Bootstrap 5**: A popular CSS framework for responsive and modern designs.


## Code Overview

- **`main.py`**: The main application file containing routes, models, and form handling.
- **`templates/`**: Contains HTML templates for rendering the pages.
- **`static/`**: (If used) Contains static files such as CSS, JavaScript, and images.


## Installation

### Prerequisites

Make sure you have Python installed on your machine. This project is compatible with Python 3.7 and above.

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/cafe-wifi-website.git
   cd cafe-wifi-website
   ```

2. **Create a Virtual Environment**

   On Windows:

   ```bash
   python -m venv venv
   ```

   On MacOS/Linux:

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On MacOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the Database**

   Run the following command to create the database and tables:

   ```bash
   flask shell
   ```

   Inside the Flask shell, execute:

   ```python
   from main import db
   db.create_all()
   exit()
   ```

## Usage

1. **Run the Application**

   ```bash
   python main.py
   ```

   The application will start on `http://127.0.0.1:5000`.

2. **Navigate the Application**

   - **Home Page**: `http://127.0.0.1:5000/` - Shows a general overview.
   - **All Cafes**: `http://127.0.0.1:5000/all` - Lists all cafes with search functionality.
   - **Random Cafe**: `http://127.0.0.1:5000/random` - Displays a random cafe from the database.
   - **Add Cafe**: `http://127.0.0.1:5000/add` - Form to add a new cafe.
   - **Delete Cafe**: `http://127.0.0.1:5000/report-closed/<cafe_id>` - Endpoint to delete a cafe.
