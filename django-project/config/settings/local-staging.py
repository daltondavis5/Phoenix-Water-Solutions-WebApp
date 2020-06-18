from .base import *
import environ

env = environ.Env()
env.read_env()

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]
