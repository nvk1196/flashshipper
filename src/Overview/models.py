from django.db import models
from django.conf import settings

BOX_OPTIONS = (
  ('1','tiny (Evolope)'),
  ('2','small'),
  ('3','medium_side'),
  ('4','medium_normal'),
  ('5','large_normal'),
  ('6','large_gamebox'),
)

class Shipper(models.Model):
	bag_number			= models.IntegerField(blank=True, null=True)								 #each bag is a unique number
	shipper_note 		= models.CharField(max_length=300, blank=True, null=True, help_text ="Optional")
	pickup_time 		= models.DateTimeField(auto_now=True)
	shipper_name		= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, editable=False)
	def __str__(self):
		return "Id: " + str(self.id)

class Packager(models.Model):
	package_time	= models.DateTimeField(auto_now=True)
	size_is_match	= models.BooleanField(blank=True, default=True)
	box_use			= models.CharField(max_length=100, blank=True, choices=BOX_OPTIONS, help_text ="If box size is not match, then what box used")
	packager_note 	= models.CharField(max_length=300, blank=True, null=True, help_text ="Optional")
	packager_name	= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, editable=False)
	tracking_number	= models.CharField(max_length=300, blank=True, default="", null=True, help_text ="They all neeed tracking")
	phone_number	= models.CharField(max_length=50, blank=True, null=True, editable=False)
	def __str__(self):
		return "Id: " + str(self.id)

class Customer_Request(models.Model):
	#---Shipper fill in---
	is_picking_up		= models.BooleanField(blank=True, default=False, help_text ="Shipper check this box and save BEFORE leaving to pick up")
	pick_up_info  		= models.OneToOneField(Shipper, on_delete=models.CASCADE, blank=True, null=True, help_text ="Shipper fill in after pick up")

	#--Packager fill in---
	is_packaged			= models.BooleanField(blank=True, default=False, help_text ="Packager check this box when package item")
	package_info 		= models.OneToOneField(Packager, on_delete=models.CASCADE, blank=True, null=True, 
						  help_text ="Packager fill in when package. If none apply, click save anyway")

	request_time		= models.DateTimeField(auto_now_add=True)	
	#how much customer should pay
	cost 	 			= models.DecimalField(decimal_places=2, max_digits=10000, help_text ="Put in real cost if item size doesn't fit in box")
	est_item_size		= models.CharField(max_length=150, blank=True, help_text ="Put in real size if item size doesn't fit in box")
	#Pickup address
	pick_up_full_name	= models.CharField(max_length=150, blank=False, null=True)
	pick_up_address		= models.CharField(max_length=150, blank=False, null=True)
	pick_up_city		= models.CharField(max_length=100, blank=False, null=True)		#each shipper responsible to pick up at 1 zipcode
	pick_up_state 		= models.CharField(max_length=100, blank=False, null=True)
	pick_up_zip			= models.CharField(max_length=100, blank=False, null=True)
	#case 1: Amazon return
	amazon_QR			= models.FileField(blank=True, null=True, upload_to='amazon_QR/%y/%m/%d')	
	#case 2: Regular return.
	return_label_1		= models.FileField(blank=True, null=True, upload_to='return_label/%y/%m/%d')	#case 2: Regular return
	return_label_2		= models.FileField(blank=True, null=True, upload_to='return_label/%y/%m/%d')
	#case 3: Regular return with package.
	fragile				= models.BooleanField(blank=True)
	#Case 4: Regular Ship -> Ship to address
	ship_to_full_name	= models.CharField(max_length=150, blank=True, null=True)
	ship_to_address		= models.CharField(max_length=150, blank=True, null=True)
	ship_to_city		= models.CharField(max_length=50, blank=True, null=True)
	ship_to_state 		= models.CharField(max_length=50, blank=True, null=True)
	ship_to_zip			= models.CharField(max_length=50, blank=True, null=True)
	ship_to_note		= models.CharField(max_length=150, blank=True, null=True)
	#verify customer phone
	phone_number		= models.CharField(max_length=50, blank=True, null=True, editable=False)
	verify_code 		= models.CharField(max_length=10, blank=True, null=True, editable=False)

	def __str__(self):
		temp = str(self.pick_up_zip) + " " + str(self.pick_up_address) 
		return str(self.id)

