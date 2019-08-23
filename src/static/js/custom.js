//prevent resubmit on refresh
if ( window.history.replaceState ) 
{
	window.history.replaceState( null, null, window.location.href );
}
	//---Main. Home----
	var need_package = new Boolean(false);
	var need_fragile = new Boolean(false);
	var est_item_size;
	var counter = 0; 

	function nextForm(current_form) {
		cal_total_cost();

	if (current_form == "PickUpForm")
	{
		if (document.getElementById("pick_up_full_name").value == "" ||
			document.getElementById("pick_up_address").value == "" ||
			document.getElementById("pick_up_state").value == "" ||
			document.getElementById("pick_up_city").value == "" ||
			document.getElementById("pick_up_zip").value == "")
			{document.getElementById("empty_field_pick_up").style.display = "block"; return false;}

		document.getElementById("pickup_form").style.display = "none";
		document.getElementById("question_form").style.display = "block";
	}
//Return
	else if (current_form == "QuestionForm_yes")	//it is a return
	{
		document.getElementById("question_form").style.display = "none";
		document.getElementById("amazon_form").style.display = "block";		
	}	
	
	else if (current_form == "Amazon_yes")		//from Amazon
	{
		document.getElementById("amazon_form").style.display = "none";
		document.getElementById("amazon_upload_form").style.display = "block";	
	}
	else if (current_form == "ReturnAmazonForm")		//upload Amazon QR code
	{
		if (document.getElementById("amazon_QR").value == "")
			{document.getElementById("empty_field_amazon_qr").style.display = "block"; return false;}

		document.getElementById("amazon_upload_form").style.display = "none";
		cal_total_cost();
		document.getElementById("total_cost_form").style.display = "block";
	}
	

	else if (current_form == "Amazon_no")			//not Amazon return	
	{
		document.getElementById("amazon_form").style.display = "none";
		document.getElementById("upload_label_form").style.display = "block";		
	}		
	else if (current_form == "UploadLabelForm")			//not Amazon return	
	{
		if (document.getElementById("return_label_1").value == "")
			{document.getElementById("empty_field_upload_label").style.display = "block"; return false;}
		document.getElementById("upload_label_form").style.display = "none";
		document.getElementById("repackage_form").style.display = "block";		
	}
	else if (current_form == "Repackage_yes")		//if need repackage
		{	need_package = true;
			document.getElementById("repackage_form").style.display = "none";
			document.getElementById("is_small_form").style.display = "block";

		}
	else if (current_form == "Repackage_no")		//don't need repackage
	{
		document.getElementById("repackage_form").style.display = "none";
		cal_total_cost();
		document.getElementById("total_cost_form").style.display = "block";

	}
	else if (current_form == "IsSmallForm_yes")		//item small enough?
	{
		document.getElementById("is_small_form").style.display = "none";
		document.getElementById("choose_size_form").style.display = "block";		
	}	
	else if (current_form == "IsSmallForm_no")		//if no. don't ship
	{
		document.getElementById("is_small_form").style.display = "none";
		document.getElementById("is_not_small_form").style.display = "block";		
	}
	else if (current_form == "ChooseSizeForm")		//if yes
	{
		//est_item_size = document.getElementByName("item_size");
		
		var elements = document.getElementsByName("item_size");
		for (var i = 0, l = elements.length; i < l; i++)
		{
    		//alert("not in");
    		if (elements[i].checked)
    		{
    			est_item_size = elements[i].value;
    		}
    	}
   	 	//alert(est_item_size);
		document.getElementById("est_item_size").value = est_item_size;		//set input value for est_item_size
		//alert("i'm in: " + est_item_size);
		document.getElementById("choose_size_form").style.display = "none";
		document.getElementById("fragile_form").style.display = "block";		

	}
	else if (current_form == "FragileForm_yes")			//if is fragile
	{
		need_fragile = true;
		document.getElementById("fragile_form").style.display = "none";
		cal_total_cost();
		document.getElementById("total_cost_form").style.display = "block";

		document.getElementById("fragile").value = "True";		//set input value for est_item_size
	}
	else if (current_form == "FragileForm_no")			//if not fragile		
	{
		document.getElementById("fragile_form").style.display = "none";
		cal_total_cost();
		document.getElementById("total_cost_form").style.display = "block";

	}

	//COMMON
	else if (current_form == "TotalCostForm")
	{
		document.getElementById("total_cost_form").style.display = "none";
		document.getElementById("enter_phone_form").style.display = "block";
	}
	else if (current_form == "EnterPhoneForm")
	{
		if (document.getElementById("phone_number").value == "")
			{document.getElementById("empty_field_enter_phone").style.display = "block"; return false;}
		document.getElementById("enter_phone_form").style.display = "none";
		document.getElementById("verify_phone_form").style.display = "block";
	}	
	else if (current_form == "SubmitForm")
	{	
		if (document.getElementById("verify_code").value == "")
			{document.getElementById("empty_field_enter_code").style.display = "block"; return false;}
		document.getElementById("verify_phone_form").style.display = "none";
		document.getElementById("final_form").style.display = "block";

		//if(phone_phone_verification = correct) -> submit this form
		// var form = document.getElementById("CustomerRequest");	//submit this form
		// form.submit();
		// form.reset();
		// window.location.href = "/user_message.html";


	}
	
	//Regular Ship
	else if (current_form == "QuestionForm_no")
	{
		document.getElementById("question_form").style.display = "none";
		document.getElementById("shipto_form").style.display = "block";		
	}
	else if (current_form == "ShipToForm")
	{	
		if (document.getElementById("ship_to_full_name").value == "" ||
			document.getElementById("ship_to_address").value == "" ||
			document.getElementById("ship_to_state").value == "" ||
			document.getElementById("ship_to_city").value == "" ||
			document.getElementById("ship_to_zip").value == "")
			{document.getElementById("empty_field_ship_to").style.display = "block"; return false;}

		need_package = true;
		document.getElementById("shipto_form").style.display = "none";
		document.getElementById("is_small_form").style.display = "block";

	}

}
	//---Calculate total cost
	function cal_total_cost(){
		var total_cost = 0.0; 
		var pick_up_fee = 4; 
		var package_fee = 2; 
		var fragile_fee = 2; 

	//pickup fee
	total_cost += pick_up_fee;
	document.getElementById("pick_up_fee").innerHTML = pick_up_fee;
	//package fee
	if (need_package == true)
	{
		document.getElementById("package_fee").innerHTML = "2";
		total_cost += 2
	}
	//fragile fee
	if (need_fragile == true)
	{
		document.getElementById("fragile_fee").innerHTML = "2";
		total_cost += 2
	}
	//shipping fee
	if 		(est_item_size == "tiny"){document.getElementById("shipping_fee").innerHTML = "7.35"; 			total_cost+= 7.35;}
	else if (est_item_size == "small"){document.getElementById("shipping_fee").innerHTML = "7.9"; 			total_cost+= 7.9;}	
	else if (est_item_size == "medium_side"){document.getElementById("shipping_fee").innerHTML = "14.35"; 	total_cost+= 14.35;}	
	else if (est_item_size == "medium_normal"){document.getElementById("shipping_fee").innerHTML = "14.35"; total_cost+= 14.35;}	
	else if (est_item_size == "large_normal"){document.getElementById("shipping_fee").innerHTML = "19.95"; 	total_cost+= 19.95;}	
	else if (est_item_size == "large_gamebox"){document.getElementById("shipping_fee").innerHTML = "19.95"; total_cost+= 19.95;}
	//total cost	
	document.getElementById("total_cost").innerHTML = "Total: " + total_cost + " $";

	document.getElementById("cost").value = total_cost;		//set input value for cost for django to pull	
}

//Send 4 digit code for phone verify without refresh. Guide: https://www.youtube.com/watch?v=KgnPSmrQrXI
var temp_phone
$(document).on('submit', '#VerifyPhoneNumber', function(e){
	e.preventDefault();
	$.ajax({
		type:'POST',
		url:'/verify_phone_number',
		data:{
			phone_number:$('#phone_number').val(),
			csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
		},
		success:function(){
			temp_phone = $('#phone_number').val();
				//alert("Sent text sms " + temp_phone);
			}
		});
});
//--Submit form to Django without reload
$(document).on('submit', '#CustomerRequest', function(e){
	e.preventDefault();
	$.ajax({
		type:'POST',
		url:'/create_request',
		data:{
				pick_up_full_name:$('#pick_up_full_name').val(),	//This stuff will pass data from html-> views.py
				pick_up_address:$('#pick_up_address').val(),
				pick_up_city:$('#pick_up_city').val(),
				pick_up_state:$('#pick_up_state').val(),
				pick_up_zip:$('#pick_up_zip').val(),
				amazon_QR:$('#amazon_QR').val(),
				return_label_1:$('#return_label_1').val(),
				return_label_2:$('#return_label_2').val(),
				est_item_size:$('#est_item_size').val(),
				fragile:$('#fragile').val(),
				ship_to_full_name:$('#ship_to_full_name').val(),
				ship_to_address:$('#ship_to_address').val(),
				ship_to_city:$('#ship_to_city').val(),
				ship_to_state:$('#ship_to_state').val(),
				ship_to_zip:$('#ship_to_zip').val(),
				ship_to_note:$('#ship_to_note').val(),
				cost:$('#cost').val(),
				// phone number needs to be on its own ajax function
				phone_number:temp_phone,
				verify_code:$('#verify_code').val(),
				csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
			},
			success:function(data){
				var response = JSON.parse(data)
				if (response["message"]==false) {
					alert("Phone number verification failed!");
					// make sure this will loop the phone number ajax function again and again
				}
			}
		});
});




//-----Zoom picture on amazon upload form-----
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("amazon_screenshot");
var modalImg = document.getElementById("amazon_screenshot_modal");
var captionText = document.getElementById("caption");
img.onclick = function(){
	modal.style.display = "block";
	modalImg.src = this.src;
} 

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
	if (event.target == modal) {
		modal.style.display = "none";
	}

}


