# 1. Install dependencies

## 1.1. Create virtual environment

## 1.2. Activate this environment
`.venv/Scripts/activate`

# 2. Start project with Django
## 2.1. Name
- ```django-admin startproject <project_name>```
## 2.2. Install single app "api"
- `python manage.py startapp api`
## 2.3. Go to [setting file](backend_django\backend_django\settings.py) path
Import below libraries.
```java
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()
```

- Also setting up for JWT:

```java
ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}
// expirated duration of jwt
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

- For connecting with frontend as well:
```java
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True
```
