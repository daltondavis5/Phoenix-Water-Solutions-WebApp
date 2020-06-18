from .base import *

#TODO: set ALLOWED_HOSTS

print(" ".join(os.environ.get('SECRET_KEY')))
print(" ".join(os.environ.get('DB_HOST')))
print(" ".join(os.environ.get('DB_NAME')))
print(" ".join(os.environ.get('DB_USER')))
print(" ".join(os.environ.get('DB_PASS')))
