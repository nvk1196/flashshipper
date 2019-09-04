from django.contrib import admin
from django.contrib.auth.models import User
from send_sms.send_sms import send_text
from django.utils.html import format_html


#from django.contrib.auth.models import Group
from .models import Customer_Request, Packager, Shipper, Internal_Tool

class Customer_RequestAdmin(admin.ModelAdmin):
	def show_google_map_url(self, obj):
		return format_html("<a href='{url}' target={OpenNewTab}>Click here for directions</a>", url= "https://www.google.com/maps/dir//" +
			   str(obj.pick_up_address) + " " + str(obj.pick_up_city) + " " + str(obj.pick_up_state) + " " + str(obj.pick_up_zip), OpenNewTab="blank")

	show_google_map_url.short_description = "Google Map"

	def is_packaged(self, obj):
		this_customer_request_id = obj.id
		this_packager = Packager.objects.get(id=this_customer_request_id)
		print("----" + str(this_packager.box_use) + "------")
		#if this_packager.box_use == "":        #LOCALHOST
		if this_packager.box_use == None:       #PRODUCTION
			return "Yes"
		else:
			return "No"

	fieldsets = (
		(None, {
			"fields": ("is_picking_up",),
		}),

		("Customer address", {
			"classes": ("collapse",),
			"fields": ("pick_up_full_name", "pick_up_address",  "pick_up_state", "pick_up_city", "pick_up_zip", "show_google_map_url"),
		}),

		("Picking up", {
			"classes": ("collapse",),
			"fields": ( "est_item_size", "cost", "after_pick_up", )
		}),
		("Packaging", {
			"classes": ("collapse",),
			"fields": ("ship_to_full_name", "ship_to_address",  "ship_to_state", "ship_to_city", "ship_to_zip", "ship_to_note",
						"amazon_QR", "return_label_1",  "return_label_2", "fragile", "after_package"),
		}),
		("Other info", {
			"classes": ("collapse",),
			"fields": ( "request_time", "phone_number", "verify_code",)
		}),
	)

	list_display	= ["id", "is_picking_up", "pick_up_zip", "is_packaged"]
	list_filter 	= ["request_time", "is_picking_up", ]
	#list_editable	= [""]
	readonly_fields	= ["request_time", "phone_number", "verify_code", "show_google_map_url",
						"amazon_QR", "return_label_1",  "return_label_2",]
	search_fields 	= ["pick_up_zip",]
	#exclude			= ["" ]



#"pick_up_full_name", "pick_up_address", "pick_up_city", "pick_up_state", "pick_up_zip",
#"ship_to_full_name", "ship_to_address", "ship_to_city", "ship_to_state", "ship_to_zip",]



class PackagerAdmin(admin.ModelAdmin):
	list_display	= ["id", "package_time", "box_use", "packager_name",]
	readonly_fields	= ["packager_name", "package_time"]
	exclude			= ["phone_number"]
	list_filter 	= ["package_time"]
	search_fields 	= ["id",]
	def save_model(self, request, obj, form, change):	#set shipper_name base on who saved Shipper table
		if not obj.packager_name:
			obj.packager_name = request.user
		obj.last_modified_by = request.user
		#Send tracking to user when save tracking number at Packager
		if obj.tracking_number != None:
			usps_link = "https://tools.usps.com/go/TrackConfirmAction?tLabels="		#tracking services link. http://www.erchov.com/ShipmentTracking.asp
			message = "Flash Shipper - Request ID: " + str(obj.id) + " - Your package tracking number is : " + usps_link + str(obj.tracking_number)
			send_text(message, obj.phone_number)
			print("Tracking Number Sent!")
		obj.save()

class ShipperAdmin(admin.ModelAdmin):
	list_display	= ["id", "pickup_time", "bag_number", "shipper_name", ]
	readonly_fields	= ["shipper_name", "pickup_time"]
	list_filter 	= ["pickup_time",]
	search_fields 	= ["bag_number", "id",]
	def save_model(self, request, obj, form, change):	#set shipper_name base on who saved Shipper table
		if not obj.shipper_name:
			obj.shipper_name = request.user
		obj.last_modified_by = request.user
		obj.save()

class Internal_ToolAdmin(admin.ModelAdmin):
		list_display	= ["title", "link"]


# Register your models here.
admin.site.register(Customer_Request, Customer_RequestAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Packager, PackagerAdmin)
admin.site.register(Internal_Tool, Internal_ToolAdmin)


