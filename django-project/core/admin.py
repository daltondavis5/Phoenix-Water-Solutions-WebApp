from django.contrib import admin
from core.models.utilityprovider import *
from core.models.property import *
from core.models.tenant import *

admin.site.register(Provider)
admin.site.register(Utility)
admin.site.register(UtilityProvider)
admin.site.register(Location)
admin.site.register(Property)
admin.site.register(PropertyUtilityProviderInfo)
admin.site.register(Unit)
admin.site.register(Meter)
admin.site.register(MeterRead)
admin.site.register(MeterError)
admin.site.register(NewAccountFee)
admin.site.register(LateFee)
admin.site.register(AdminFee)
admin.site.register(Tenant)
admin.site.register(TenantCharge)
admin.site.register(PaymentMethod)
admin.site.register(Payment)
admin.site.register(TenantChargePayment)
admin.site.register(TenantNotes)
