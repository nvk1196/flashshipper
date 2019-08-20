from django.contrib import admin
from .models import Overview, Customer_Request, Shipper, Packager

# Register your models here.
admin.site.register(Overview)
admin.site.register(Customer_Request)
admin.site.register(Shipper)
admin.site.register(Packager)
