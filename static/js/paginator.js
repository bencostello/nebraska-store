$(document).ready(function(){
	var pages;
	var total = "{{total_pages}}";
	var category = "{{category}}";
	var maxPages = parseInt(total,10);
	if (maxPages < 100) {
		pages = maxPages;
	}
	else {
		pages = 100;
	}
	var html = "<li class='disabled'><a id='arrowFirst' href='/1'><i class='material-icons'>chevron_left</i></a></li><li class='active'><a href='/1'>1</a></li>";
	for (var i=2; i < pages+1; i++) {
			html += "<li class='waves-effect'><a href='/category/"+category+i+"'>"+i+"</a></li>";
		}
		html+="<li class='waves-effect'><a id='arrowLast' href='/"+pages+"'><i class='material-icons'>chevron_right</i></a></li>"
	$('.pagination').append(html);

	var url = window.location.href;
	var result = '/' + url.split('/')[5];
	$(".pagination li").removeClass("active");
	$(".pagination li a[href='" + result + "']").parent().addClass("active");
	$(".pagination li #arrowFirst, .pagination li #arrowLast").parent().removeClass("active");

	if (result == '/1' || result == '/') {
		$(".pagination li #arrowFirst").parent().addClass("disabled");
		$(".pagination li a:eq(1)").parent().addClass("active");
	}
	else{
		$(".pagination li #arrowFirst").parent().removeClass("disabled");
	}

	var last = result.split('/')[1];
	if (parseInt(last) == pages) {
		$(".pagination li #arrowLast").parent().addClass("disabled");
	}
	else{
		$(".pagination li #arrowLast").parent().removeClass("disabled");
	}
});
