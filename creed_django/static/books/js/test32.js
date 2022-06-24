$( document ).ready(function() {	
$('#myCustomId').hide();
$('label[for="myCustomId"]').hide();
$('#myCustomIdone').hide();
$('label[for="myCustomIdone"]').hide();
$('#myCustomIdtwo').hide();
$('label[for="myCustomIdtwo"]').hide();
   $("#id_sector_your_instution_belongs").change(function() {
   if ($(this).val() === "Others") {  
	  $('#myCustomId').show();
      $('label[for="myCustomId"]').hide();
     
	  }	else {
                $('#myCustomId').hide();
				$('label[for="myCustomId"]').hide();
				
            }
			
		
    });
	
	$("#id_mandate_of_institution").change(function() {
   if ($(this).val() === "Others (specify)") {  
	  $('#myCustomIdone').show();
      $('label[for="myCustomIdone"]').hide();
     
	  }	else {
                $('#myCustomIdone').hide();
				$('label[for="myCustomIdone"]').hide();
				
            }
			
		
    });
	
	$("#id_Category_of_technologies").change(function() {
   if ($(this).val() === "Others (specify)") {  
	  $('#myCustomIdtwo').show();
      $('label[for="myCustomIdtwo"]').hide();
     
	  }	else {
                $('#myCustomIdtwo').hide();
				$('label[for="myCustomIdtwo"]').hide();
				
            }
			
		
    });
    console.log( "test!" );
});