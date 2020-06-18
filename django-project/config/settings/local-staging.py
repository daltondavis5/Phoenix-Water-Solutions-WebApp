from .base import *
import environ

env = environ.Env()
env.read_env()

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

print (os.environ.get('SECRET_KEY'))
print (os.environ.get('DB_HOST'))
print (os.environ.get('DB_NAME'))
print (os.environ.get('DB_USER'))
print (os.environ.get('DB_PASS'))
