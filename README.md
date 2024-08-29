# Todos Application

This is a simple Todo application built with FastAPI for the backend and React with Chakra UI for the frontend. The application allows users to create, update, delete, and view a list of todo items.

## Features

- **Add Todo**: Users can add a new todo item to the list.
- **View Todos**: The application displays all existing todo items.
- **Update Todo**: Users can update the content of a todo item.
- **Delete Todo**: Users can delete a todo item.

## Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: React, Chakra UI
- **Database**: SQLite (or any other configured database)
- **HTTP Client**: Fetch API

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js 14+
- npm

### Backend Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/todos-app.git
    cd todos-app/backend
    ```

2. **Create a virtual environment**:

    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the FastAPI server**:

    ```sh

    uvicorn app.main:app --reload
    ```

   The server will be running at `http://localhost:8000`.

### Frontend Setup

1. **Navigate to the frontend directory**:

    ```sh
    cd ../frontend
    ```

2. **Install dependencies**:

    ```sh
    npm install
    ```

3. **Run the React app**:

    ```sh
    npm start
    ```

   The application will be available at `http://localhost:3000`.

## Usage

- **Add a Todo**: Type a task in the input box and click "Add Todo".
- **Update a Todo**: Click the "Update Todo" button next to a task, edit the content, and click "Update Todo".
- **Delete a Todo**: Click the "Delete Todo" button next to a task to remove it.

## Project Structure

```plaintext
todos-app/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   └── todo.py
│   │   │   └── routers.py
│   │   ├── core/
│   │   ├── crud/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   └── index.js
    └── package.json