from decouple import config
from .base import *


APP_URL = "https://prathamesh-inventory-management.azurewebsites.net"
HOST_URL = "https://prathamesh-api.azurewebsites.net"

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
    'http://localhost:3000',
    'https://prathamesh-inventory-management.azurewebsites.net'
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "ocp-apim-subscription-key",
]
