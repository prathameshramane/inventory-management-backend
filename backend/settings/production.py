from decouple import config
from .base import *


APP_URL = "http://localhost:3000"
HOST_URL = "http://127.0.0.1:8000"

DEBUG = False

ALLOWED_HOSTS = ['prathamesh-api.azurewebsites.net']

# Database

DATABASES = {
    'default': {
        "ENGINE": "mssql",
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_USER_PASSWORD'),
        'HOST': 'get-assessment-server.database.windows.net',
        "PORT": "1433",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
        }
    }
}


# CORS

CORS_ALLOWED_ORIGINS = [
]
