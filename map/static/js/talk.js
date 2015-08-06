function fundget_box_show(msg){
    var postion_y = $('.pork-guy').position()['top'] + 20;
    $('#fundget-box').css("margin-top", postion_y).find('.msg').text(msg).end().show();
}


$("label[for='profit-distribut']").on('mouseover',function () {
    fundget_box_show('test');
	console.log("hahaha");
});
$("label[for='profit-distribut']").on('mouseleave',function () {
	$('#fundget-box').hide();
	console.log("hahaha");
});
