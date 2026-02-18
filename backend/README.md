# Wayffs Backend

The backend for Wayffs is built with Django and Django Rest Framework, providing a consistent and secure REST API.

## 📦 Requirements

- Python 3.11+
- PostgreSQL
- Virtual environment (recommended)

## 🔧 Local Setup (Without Docker)

If you prefer to run the backend outside of Docker:

1. **Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Copy the settings from the root `.env` or create a `.env` in this directory with your local database settings.

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start Server**:
   ```bash
   python manage.py runserver
   ```

## 🛠️ API Philosophy

- **RESTful**: Predictable endpoints and JSON-based communication.
- **Secure**: Input validation, data sanitization, and proper error handling.
- **Lightweight**: Optimized for low resource usage on AWS Free Tier.

## 📂 Structure

- `/core`: Main Django project settings and URL configuration.
- `/users`: User management and authentication.
- `/projects`: Core business logic for project management.
- `manage.py`: Django management utility.
