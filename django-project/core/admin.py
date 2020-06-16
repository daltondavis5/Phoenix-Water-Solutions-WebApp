from django.contrib import admin
from core.models.utilityprovider import *

admin.site.register(Provider)
admin.site.register(Utility)
admin.site.register(UtilityProvider)
admin.site.register(Location)
