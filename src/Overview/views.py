from django.shortcuts import render
from .models import Customer_Request

# Create your views here.
def home (request): 
	pick_up_full_name = request.POST.get("pick_up_full_name")
	pick_up_address	  = request.POST.get("pick_up_address")
	pick_up_city      = request.POST.get("pick_up_city")
	pick_up_state     = request.POST.get("pick_up_state")
	pick_up_zip       = request.POST.get("pick_up_zip")
	amazon_QR         = request.POST.get("amazon_QR")
	return_label_1    = request.POST.get("return_label_1")
	return_label_2    = request.POST.get("return_label_2")
	est_item_size	  = request.POST.get("est_item_size")
	fragile_temp	  = request.POST.get("fragile")			#can't typecase boolean so gotta use this
	if fragile_temp	  == "True":
		fragile 	  = True
	elif fragile_temp == "False":
		fragile 	  = False	
	ship_to_full_name = request.POST.get("ship_to_full_name")
	ship_to_address   = request.POST.get("ship_to_address")
	ship_to_city 	  = request.POST.get("ship_to_city")
	ship_to_state	  = request.POST.get("ship_to_state")
	ship_to_zip		  = request.POST.get("ship_to_zip")
	ship_to_note	  = request.POST.get("ship_to_note")
	cost			  = float(request.POST.get("cost"))
	#customer_phone	  = request.POST.get("customer_phone")		
	#create a Request model
	CustomerRequest   = Customer_Request(
		pick_up_full_name=pick_up_full_name,
		pick_up_address=pick_up_address,
		pick_up_city=pick_up_city,
		pick_up_state=pick_up_state,
		pick_up_zip=pick_up_zip,
		amazon_QR=amazon_QR,
		return_label_1=return_label_1,
		return_label_2=return_label_2,
		est_item_size=est_item_size,
		fragile=fragile,
		ship_to_full_name=ship_to_full_name,
		ship_to_address=ship_to_address,
		ship_to_city=ship_to_city,
		ship_to_state=ship_to_state,
		ship_to_zip=ship_to_zip,
		ship_to_note=ship_to_note,
		cost=cost)	
	CustomerRequest.save()
	return render(request, 'home.html')

def user_message (request):
	return render(request, 'user_message.html')

