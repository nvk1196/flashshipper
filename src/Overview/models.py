from django.db import models


class Request(models.Model):
	#General info	
	request_time		= models.DateTimeField(auto_now_add=True)	

	#Pickup address
	pick_up_full_name	= models.CharField(max_length=150, blank=False)
	pick_up_address		= models.CharField(max_length=150, blank=False)
	pick_up_city		= models.CharField(max_length=100, blank=False)
	pick_up_state 		= models.CharField(max_length=100, blank=False)
	pick_up_zip			= models.CharField(max_length=100, blank=False)

	#Return item?
	#return_item			= models.BooleanField(blank=False)

	#Amazon return
	#amazon_return		= models.BooleanField(blank=False)
	amazon_QR			= models.FileField(blank=True)	#case 1: Amazon return

	#Regular return
	return_label_1		= models.FileField(blank=True)	#case 2: Regular return
	return_label_2		= models.FileField(blank=True)
	#repackage			= models.BooleanField(blank=False)

	#Package
	est_item_size		= models.CharField(max_length=150, blank=True)	#case 3: Regular return with pakakge
	fragile				= models.BooleanField(blank=True)

	#Regular Ship -> Ship to address
	ship_to_full_name	= models.CharField(max_length=150, blank=True)	#case 4: Regular ship
	ship_to_address		= models.CharField(max_length=150, blank=True)
	ship_to_city		= models.CharField(max_length=50, blank=True)
	ship_to_state 		= models.CharField(max_length=50, blank=True)
	ship_to_zip			= models.CharField(max_length=50, blank=True)

	#Estimate cost
	est_cost 			= models.DecimalField(decimal_places=3, max_digits=10000)


class Shipper(models.Model):
	is_picked_up	= models.BooleanField(default=False)					#this trigger to create this object instance
	pickup_time 	= models.DateTimeField(auto_now_add=True)	
	shipper_name	= models.CharField(max_length=100)
	bag_number		= models.IntegerField();								 #each shipper has a unique bag number

# 	pick_up_address		(cant refenrece Request table. Have to get it from user when they enter)
# 	est_item_size		(reference Request table. Shipper can edit if this info is not correct)
#	est_cost			(reference Request table. Shipper can edit if this info is not correct)

class Packager(models.Model):
	package_time	= models.DateTimeField(auto_now_add=True)
	box_use			= models.CharField(max_length=100)
	size_is_match	= models.BooleanField(blank=False)
	is_packaged		= models.BooleanField(default=False)

	#request  			= models.ForeignKey(Request, on_delete=models.CASCADE, blank=True, null=True)
	#shipper  			= models.ForeignKey(Shipper, on_delete=models.CASCADE, blank=True, null=True)

#String 		bag_id				(reference Shipper table)	
#String 		item_size			(reference Shipper table)


class Overview(models.Model):
	Request  			= models.ForeignKey("Request", on_delete=models.CASCADE, blank=True, null=True)
	Shipper  			= models.ForeignKey("Shipper", on_delete=models.CASCADE, blank=True, null=True)
	Packager  			= models.ForeignKey("Packager", on_delete=models.CASCADE, blank=True, null=True)
