from django.shortcuts import render
from .models import Customer_Request, Shipper, Packager
from django.http import HttpResponse
from send_sms.send_sms import send_text
from django.template.loader import get_template
from random import randint
from django.views.generic import View
import json

generated_code = ""

def generate_rand_code ():
	#generate random 4 digits code
	temp_code = str(randint(1000, 9999))
	global generated_code
	generated_code = temp_code		#set generated_code as generated code for create_request() to use
	return temp_code

# Create your views here.
def verify_phone_number(request):
	if request.method == "POST":
		phone_number = request.POST.get("phone_number")
	#send verify code to user phone
	message = "Flash Shipper verification code: "
	send_text(message + generate_rand_code(), phone_number)
	return HttpResponse('') 

def create_request (request): 
	if request.method == "POST":
		verify_code = request.POST.get("verify_code")
		#If the verification code is correct. Create this CustomerRequest and save in db
		print("---CODE IS-" + generated_code + "-END")
		if verify_code == generated_code:
			print("---CODE IS CORRECT. IT IS " + verify_code)
			pick_up_full_name = request.POST.get("pick_up_full_name")	#this get data from ajax data from custom.js
			pick_up_address	  = request.POST.get("pick_up_address")
			pick_up_city      = request.POST.get("pick_up_city")
			pick_up_state     = request.POST.get("pick_up_state")
			pick_up_zip       = request.POST.get("pick_up_zip")
			amazon_QR         = request.POST.get("amazon_QR")
			return_label_1    = request.POST.get("return_label_1")
			return_label_2    = request.POST.get("return_label_2")
			est_item_size	  = request.POST.get("est_item_size")
			fragile_temp	  = request.POST.get("fragile")			#can't typecast boolean so gotta use this
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
			phone_number	  = request.POST.get("phone_number")

			package_info_temp = Packager(phone_number = "+1" + phone_number)
			pick_up_info_temp = Shipper()
			package_info_temp.save()
			pick_up_info_temp.save()
			#create a Request model
			CustomerRequest   = Customer_Request(
				pick_up_full_name = pick_up_full_name,
				pick_up_address = pick_up_address,
				pick_up_city = pick_up_city,
				pick_up_state = pick_up_state,
				pick_up_zip = pick_up_zip,
				amazon_QR = amazon_QR,
				return_label_1 = return_label_1,
				return_label_2 = return_label_2,
				est_item_size = est_item_size,
				fragile = fragile,
				ship_to_full_name = ship_to_full_name,
				ship_to_address = ship_to_address,
				ship_to_city = ship_to_city,
				ship_to_state = ship_to_state,
				ship_to_zip = ship_to_zip,
				ship_to_note = ship_to_note,
				cost = cost,
				phone_number = "+1" + phone_number,
				verify_code = generated_code,
				package_info = package_info_temp,
				pick_up_info = pick_up_info_temp,
				)	
			CustomerRequest.save()
			return HttpResponse(content=json.dumps({"message": True}))

		else:
			print("---WRONG CODE")		#send an alert in html through js
			return HttpResponse(content=json.dumps({"message": False}))

def home (request):
	return render(request, 'home.html')

# def new_page (request):
# 	return render(request, 'new_page.html')

#Printing label generator
def generate_view (request, customer_request_id, *args, **kwargs):
	if request.user.is_authenticated:
		customer_request = Customer_Request.objects.get(id=customer_request_id)
		context = {
					"id"  					:customer_request.id,
					"pick_up_full_name" 	:customer_request.pick_up_full_name,
					"pick_up_address" 		:customer_request.pick_up_address,
					"pick_up_city"  		:customer_request.pick_up_city,
					"pick_up_state"  		:customer_request.pick_up_state,
					"pick_up_zip"  			:customer_request.pick_up_zip,

					"ship_to_full_name" 	:customer_request.ship_to_full_name,
					"ship_to_address" 		:customer_request.ship_to_address,
					"ship_to_city"  		:customer_request.ship_to_city,
					"ship_to_state"  		:customer_request.ship_to_state,
					"ship_to_zip"  			:customer_request.ship_to_zip,
					"ship_to_note"  		:customer_request.ship_to_note,
		}
		return render (request, 'print_label.html', context)
	else:
		return HttpResponse("<h2>You don't have permission to access this content.<h2>")

		

    # template = get_template('invoice.html')
    # context = {
    #     "invoice_id": 123,
    #     "customer_name": "John Cooper",
    #     "amount": 1399.99,
    #     "today": "Today",
    # }
    # html = template.render(context)
    # pdf = render_to_pdf('print_label.html', context)
    # if pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     filename = "Invoice_%s.pdf" %("12341231")
    #     content = "inline; filename='%s'" %(filename)
    #     download = request.GET.get("download")
    #     if download:
    #         content = "attachment; filename='%s'" %(filename)
    #     response['Content-Disposition'] = content
    #     return response
    # return HttpResponse("Not found")


