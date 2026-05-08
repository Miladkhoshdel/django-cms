# Django CMS

A simple Django-based Content Management System (CMS) project.

## 🔧 Tools Used

- Python 3.12
- Django
- `venv` for virtual environment management
- `pip` and `requirements/base.txt` for dependency management

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Miladkhoshdel/django-cms
cd django-cms
```

### 2. Create and activate a virtual environment

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements/base.txt
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Load initial settings

```bash
python manage.py loaddata initial_settings
```

### 6. Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`.
The admin panel is available at `http://127.0.0.1:8000/panel/`.

## 🌐 Web Pages

### Blog Posts

Public blog pages render only published posts.

#### List Published Posts

`GET http://127.0.0.1:8000/posts/`

#### View Single Published Post

`GET http://127.0.0.1:8000/posts/<slug>/`

## 📚 API Endpoints

### 🔑 Token Authentication

#### Obtain Token

`POST http://127.0.0.1:8000/api/token/`

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

`POST http://127.0.0.1:8000/api/token/verify/`

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

`GET http://127.0.0.1:8000/api/v1/core/settings/`

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

`GET http://127.0.0.1:8000/api/v1/core/settings/<key>/`

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

### 📝 Blog Posts API

Blog API endpoints are available under `/api/v1/blog/` and require a JWT access token:

```http
Authorization: Bearer <access_token>
```

#### Create Blog Post

`POST http://127.0.0.1:8000/api/v1/blog/posts/`

**Sample Request:**

```bash
curl -X POST http://127.0.0.1:8000/api/v1/blog/posts/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "First weblog post",
    "excerpt": "Short summary",
    "content": "Full blog post content here.",
    "status": "published"
  }'
```

**Sample Response:**

```json
{
    "id": 1,
    "title": "First weblog post",
    "slug": "first-weblog-post",
    "excerpt": "Short summary",
    "content": "Full blog post content here.",
    "status": "published",
    "published_at": "2026-05-07T14:55:00Z",
    "author": "admin",
    "created_at": "2026-05-07T14:55:00Z",
    "updated_at": "2026-05-07T14:55:00Z"
}
```

#### List Blog Posts

`GET http://127.0.0.1:8000/api/v1/blog/posts/`

**Sample Request:**

```bash
curl http://127.0.0.1:8000/api/v1/blog/posts/ \
  -H "Authorization: Bearer <access_token>"
```

**Sample Response:**

```json
[
    {
        "id": 1,
        "title": "First weblog post",
        "slug": "first-weblog-post",
        "excerpt": "Short summary",
        "content": "Full blog post content here.",
        "status": "published",
        "published_at": "2026-05-07T14:55:00Z",
        "author": "admin",
        "created_at": "2026-05-07T14:55:00Z",
        "updated_at": "2026-05-07T14:55:00Z"
    }
]
```

#### Filter Blog Posts By Status

`GET http://127.0.0.1:8000/api/v1/blog/posts/?status=published`

**Sample Request:**

```bash
curl "http://127.0.0.1:8000/api/v1/blog/posts/?status=published" \
  -H "Authorization: Bearer <access_token>"
```

**Sample Response:**

```json
[
    {
        "id": 1,
        "title": "First weblog post",
        "slug": "first-weblog-post",
        "excerpt": "Short summary",
        "content": "Full blog post content here.",
        "status": "published",
        "published_at": "2026-05-07T14:55:00Z",
        "author": "admin",
        "created_at": "2026-05-07T14:55:00Z",
        "updated_at": "2026-05-07T14:55:00Z"
    }
]
```

#### Get Single Blog Post

`GET http://127.0.0.1:8000/api/v1/blog/posts/<slug>/`

**Sample Request:**

```bash
curl http://127.0.0.1:8000/api/v1/blog/posts/first-weblog-post/ \
  -H "Authorization: Bearer <access_token>"
```

**Sample Response:**

```json
{
    "id": 1,
    "title": "First weblog post",
    "slug": "first-weblog-post",
    "excerpt": "Short summary",
    "content": "Full blog post content here.",
    "status": "published",
    "published_at": "2026-05-07T14:55:00Z",
    "author": "admin",
    "created_at": "2026-05-07T14:55:00Z",
    "updated_at": "2026-05-07T14:55:00Z"
}
```

#### Update Blog Post

`PATCH http://127.0.0.1:8000/api/v1/blog/posts/<slug>/`

**Sample Request:**

```bash
curl -X PATCH http://127.0.0.1:8000/api/v1/blog/posts/first-weblog-post/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"status":"draft"}'
```

**Sample Response:**

```json
{
    "id": 1,
    "title": "First weblog post",
    "slug": "first-weblog-post",
    "excerpt": "Short summary",
    "content": "Full blog post content here.",
    "status": "draft",
    "published_at": "2026-05-07T14:55:00Z",
    "author": "admin",
    "created_at": "2026-05-07T14:55:00Z",
    "updated_at": "2026-05-07T15:10:00Z"
}
```

#### Delete Blog Post

`DELETE http://127.0.0.1:8000/api/v1/blog/posts/<slug>/`

**Sample Request:**

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/blog/posts/first-weblog-post/ \
  -H "Authorization: Bearer <access_token>"
```

**Sample Response:**

```http
HTTP/1.1 204 No Content
```
