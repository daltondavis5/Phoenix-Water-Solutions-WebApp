from django.urls import reverse

from core.models.utilityprovider import Utility, Location, Provider, \
    UtilityProvider
from core.models.property import Unit, Meter, Property, MeterRead, \
    MeterError
from core.models.tenant import *
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
