from django.contrib import admin
from .models import Overview, Request, Shipper, Packager

# Register your models here.
admin.site.register(Overview)
admin.site.register(Request)
admin.site.register(Shipper)
admin.site.register(Packager)
