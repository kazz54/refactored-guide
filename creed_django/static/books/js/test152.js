$( document ).ready(function() {	
$('#id_other_institution_belong').hide();
$('#id_other_mandate_of_institution').hide();
$('label[for="id_other_institution_belong"]').hide();
$('label[for="id_other_mandate_of_institution"]').hide();
//$('#myCustomIdtwo').hide();
//$('label[for="myCustomIdtwo"]').hide();
   $("#id_sector_your_instution_belongs").change(function() {
   if ($(this).val() === "Others") {  
	  $('#id_other_institution_belong').show();
      $('label[for="id_other_institution_belong"]').hide();
     
	  }	else {
                $('#id_other_institution_belong').hide();
				$('label[for="id_other_institution_belong"]').hide();
				
            }
			
		
    });
	
	 $("#id_mandate_of_institution").change(function() {
   if ($(this).val() === "Others") {  
	  $('#id_other_mandate_of_institution').show();
      $('label[for="id_other_mandate_of_institution"]').hide();
     
	  }	else {
                $('#id_other_mandate_of_institution').hide();
				$('label[for="id_other_mandate_of_institution"]').hide();
				
            }
			
		
    });
	
	
	
	
    console.log( "test002!" );
});