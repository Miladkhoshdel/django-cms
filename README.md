# Django CMS

A simple Django-based Content Management System (CMS) project.

## 🔧 Tools Used

- Python 3.12
- Django
- [Poetry](https://python-poetry.org/) for dependency management

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Miladkhoshdel/django-cms
cd django-cms
```

### 2. Load Initial Settings

```bash
python manage.py loaddata initial_settings
```

## 📚 API Endpoints

### 🔑 Token Authentication

#### Obtain Token

Send a POST request to the token endpoint with your credentials:

```json
{
    "username": "<user>",
    "password": "<password>"
}
```

**Sample Response:**

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

#### Verify Token

Send a POST request to the verify endpoint with your token:

```json
{
    "token": "<access_token>"
}
```

**Sample Error Response (Expired Token):**

```json
{
    "detail": "Token is expired",
    "code": "token_not_valid"
}
```

### ⚙️ Settings

#### Get All Settings

`GET http://127.0.0.1:8000/api/v1/core/settings`

**Sample Response:**

```json
{
    "success": true,
    "data": {
        "site_title": "Django CMS",
        "site_description": "Simple Django CMS",
        "site_keywords": "Django, CMS, Python",
        "site_author": "Your Name",
        "site_logo_path": "/static/images/logo.png"
    }
}
```

#### Get Single Setting

**Sample Response:**

```json
{
    "success": true,
    "data": {
        "key": "site_keywords",
        "value": "Django, CMS, Python"
    }
}
```
