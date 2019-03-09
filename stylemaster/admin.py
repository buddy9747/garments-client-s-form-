from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Approver)
admin.site.register(PDMerchant)
admin.site.register(ProductionMerchant)
admin.site.register(FactoryMerchant)
admin.site.register(CustomGroup)
admin.site.register(Sample)
admin.site.register(Stylemaster)
admin.site.register(Fabric)
admin.site.register(Trims)
admin.site.register(BOM)