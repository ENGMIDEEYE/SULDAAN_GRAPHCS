$("body").delegate(".get_link","click",function (e) {
	e.preventDefault();    
	$(".hidechart").empty();   
    alert(1); 
	 var url = $(this).attr('href');
	 $.post(url,function(data) {
	 	$(".hidechart").html(data);
        alert(data);
    
	
	 })
});