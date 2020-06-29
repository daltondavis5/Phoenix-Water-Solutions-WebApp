from django.contrib import admin
from core.models.utilityprovider import *
from core.models.property import *

admin.site.register(Provider)
admin.site.register(Utility)
admin.site.register(UtilityProvider)
admin.site.register(Location)
admin.site.register(Property)
admin.site.register(PropertyCityUtilityInfo)
admin.site.register(Unit)
admin.site.register(Meter)
admin.site.register(MeterRead)
admin.site.register(MeterError)
admin.site.register(NewAccountFee)
admin.site.register(LateFee)
admin.site.register(AdminFee)
