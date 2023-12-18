## ToDoApp: A Flask & SQLAlchemy Powered Task Management Application

This repository hosts ToDoApp, a simple but functional to-do list application built with Flask and SQLAlchemy. It allows users to:

* **Create** tasks with optional due dates and priority levels.
* **View** a list of all tasks sorted by creation date.
* **Mark** tasks as completed.
* **Edit** the content of existing tasks.
* **Delete** tasks they no longer need.

### Prerequisites

* Python 3.8+
* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* dotenv
* PostgreSQL database (or SQLite, for basic testing)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/TuranOzdemir/ToDoApp.git
```

2. Create a `.env` file in the project root and add the following environment variables:

```
DATABASE_URL=<your_postgres_database_url>
# Alternatively, for SQLite:
#DATABASE_URL=sqlite:///todo_app.db
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create the database tables:

```bash
python3 app.py create_database
```

5. Run the application:

```bash
python3 app.py
```

**Note:** This will run the app in production mode (debug=False). For development with live reloading, set `debug=True` in the command.

### Features

* User-friendly interface built with HTML and CSS.
* Dynamic task list using Flask routes and templates.
* CRUD operations (Create, Read, Update, Delete) for tasks with SQLAlchemy models.
* Error handling for a smooth user experience.


