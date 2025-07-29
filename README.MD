````markdown
# Django Project

This is a Django web application using Daphne for ASGI deployment.

## Clone the Repository

```bash
git clone https://github.com/vishalpandhare01/Task-Management-backend.git
cd your-repo-name
````

## Setup

1. **Create and activate virtual environment**
   *(Windows example below)*

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the ASGI server with Daphne**

   ```bash
   python -m daphne config.asgi:application
   ```

## Notes

* Make sure `config` is the correct Django project folder and contains the `asgi.py` file.
* You may need to run migrations and create a superuser:

  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  ```

## Requirements File

```bash
pip freeze > requirements.txt
```

