$( document ).ready(function() {	
$('#desired_id').hide();
  $("#id_category_of_technologies").change(function() { 
    if ($(this).val() === "Laboratory") {
		$('#desired_id').show();
		
	 }  	else {
                $('#desired_id').hide();	
			}	
  
  });



    console.log( "test!" );
});