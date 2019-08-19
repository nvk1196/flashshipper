	//---Main. Home----
function nextForm(current_form) {
	if (current_form == "PickUpForm")
	{
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
		document.getElementById("amazon_upload_form").style.display = "none";
		document.getElementById("total_cost_form").style.display = "block";		
	}
	

	else if (current_form == "Amazon_no")			//not Amazon return	
	{
		document.getElementById("amazon_form").style.display = "none";
		document.getElementById("upload_label_form").style.display = "block";		
	}		
	else if (current_form == "UploadLabelForm")			//not Amazon return	
	{
		document.getElementById("upload_label_form").style.display = "none";
		document.getElementById("repackage_form").style.display = "block";		
	}
	else if (current_form == "Repackage_yes")		//if need repackage
	{
		document.getElementById("repackage_form").style.display = "none";
		document.getElementById("is_small_form").style.display = "block";		
	}
	else if (current_form == "UploadLabelForm")		//if need repackage
	{
		document.getElementById("upload_label_form").style.display = "none";
		document.getElementById("is_small_form").style.display = "block";		
	}
	else if (current_form == "Repackage_no")		//don't need repackage
	{
		document.getElementById("repackage_form").style.display = "none";
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
		document.getElementById("choose_size_form").style.display = "none";
		document.getElementById("fragile_form").style.display = "block";		
	}
	else if (current_form == "FragileForm_yes")			//if is fragile
	{
		document.getElementById("fragile_form").style.display = "none";
		document.getElementById("total_cost_form").style.display = "block";		
	}
	else if (current_form == "FragileForm_no")			//if not fragile		
	{
		document.getElementById("fragile_form").style.display = "none";
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
		document.getElementById("enter_phone_form").style.display = "none";
		document.getElementById("verify_phone_form").style.display = "block";
	}	
		else if (current_form == "VerifyPhoneForm")
	{
		document.getElementById("verify_phone_form").style.display = "none";
		document.getElementById("final_form").style.display = "block";
	}
	
	//Regular Ship
		else if (current_form == "QuestionForm_no")
	{
		document.getElementById("question_form").style.display = "none";
		document.getElementById("shipto_form").style.display = "block";		
	}
		else if (current_form == "ShipToForm")
	{
		document.getElementById("shipto_form").style.display = "none";
		document.getElementById("is_small_form").style.display = "block";		
	}	
}

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


