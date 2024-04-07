# Django REST Framework Example

This is a simple example project demonstrating how to build a RESTful API with Django and Django Rest Framework (DRF), using SQLite as the database.

## Setup

1. **Clone the repository:**
    ```
    git clone https:/juliokozarewicz/github.com/apibook.git
    ```

2. **Navigate to the project directory:**
    ```
    cd apibook
    ```

3. **Create a virtual environment (optional but recommended):**
    ```
    python -m venv venv
    ```

4. **Activate the virtual environment:**
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source venv/bin/activate
        ```

5. **Install the project dependencies (if it exists):**
    ```
    pip install -r requirements.txt
    ```

6. **Apply migrations to set up the SQLite database:**
    ```
    python manage.py migrate
    ```

7. **Run the development server:**
    ```
    python manage.py runserver
    ```

8. **Access the API in your web browser or via tools like cURL or Postman:**
    ```
    http://127.0.0.1:8000/api/
    ```

## Dependencies

- Django
- Django Rest Framework

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.
