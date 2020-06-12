from .base import *
import environ

env = environ.Env()
env.read_env()

SECRET_KEY = env('SECRET_KEY')
