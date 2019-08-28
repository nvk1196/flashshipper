from django.contrib import admin
from django.contrib.auth.models import User
from send_sms.send_sms import send_text


#from django.contrib.auth.models import Group
from .models import Customer_Request, Packager, Shipper

class Customer_RequestAdmin(admin.ModelAdmin):
	list_display	= ["id", "is_picking_up", "pick_up_zip", "pick_up_address", "is_packaged"]
	readonly_fields	= ["request_time", "phone_number", "verify_code"]
	list_filter 	= [ "request_time", "pick_up_zip", "is_picking_up", "is_packaged",]
	#exclude		= ["", ]
	#search_fields 	= ["",]
	

class PackagerAdmin(admin.ModelAdmin):
	list_display	= ["id", "package_time", "size_is_match", "packager_name"]
	readonly_fields	= ["packager_name", ]
	list_filter 	= ["package_time", "size_is_match"]
	search_fields 	= ["id",]
	def save_model(self, request, obj, form, change):	#set shipper_name base on who saved Shipper table
		if not obj.packager_name:
			obj.packager_name = request.user
		obj.last_modified_by = request.user
		#Send tracking to user when save tracking number at Packager
		if obj.tracking_number != None:
			usps_link = "https://tools.usps.com/go/TrackConfirmAction?tLabels="		#tracking services link. http://www.erchov.com/ShipmentTracking.asp
			message = "Flash Shipper - Your package tracking number is : " + usps_link + str(obj.tracking_number)
			send_text(message, obj.phone_number)
			print("Tracking Number Sent!")
		obj.save()

class ShipperAdmin(admin.ModelAdmin):
	list_display	= ["id", "pickup_time", "bag_number", "shipper_name", ]
	readonly_fields	= ["shipper_name",]
	list_filter 	= ["pickup_time",]
	search_fields 	= ["bag_number", "id",]
	def save_model(self, request, obj, form, change):	#set shipper_name base on who saved Shipper table
		if not obj.shipper_name:
			obj.shipper_name = request.user
		obj.last_modified_by = request.user
		obj.save()

# Register your models here.
admin.site.register(Customer_Request, Customer_RequestAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Packager, PackagerAdmin)

