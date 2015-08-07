function fundget_box_show(){
    var postion_y = $('.pork-guy').position()['top'] + 20;
    $('#talk-box').css("margin-top", postion_y).show();
}
function diagram_box_show(){
    var postion_y = $('#diagram').position()['top'] + 70;
    $('#diagram-explain').css("margin-top", postion_y).show();
}
function displayNextImage() {
    x = (x === images.length - 1) ? 0 : x + 1;
        $('#pork-guy-pic').attr("src", images[x]);
}
function displayPreviousImage() {
    x = (x <= 0) ? images.length - 1 : x - 1;
        // document.getElementById("#pork-guy-pic").src = images[x];
        $('#pork-guy-pic').attr("src", images[x]);
}

var images = [], x = -1;
images[0] = "/static/img/pigman3.png";
images[1] = "/static/img/pigman2.png";
var timer = 0;
//回饋金介紹
$("label[for='profit-distribut']").on('mouseover',function () {
	fundget_box_show();
	timer = setInterval(displayNextImage, 200);
	$('.fundget-msg').show();
});
$("label[for='profit-distribut']").on('mouseleave',function () {
	$('#talk-box').hide();
	$('.fundget-msg').hide();
	clearInterval(timer);
	$('#pork-guy-pic').attr("src","/static/img/pigman2.png");
});

//盈餘分配介紹
$("label[for='charity']").on('mouseover',function () {
	fundget_box_show();
	timer = setInterval(displayNextImage, 200);
	$('.profit-msg').show();
});
$("label[for='charity']").on('mouseleave',function () {
	$('#talk-box').hide();
	$('.profit-msg').hide();
	clearInterval(timer);
	$('#pork-guy-pic').attr("src","/static/img/pigman2.png");
});

//頭獎次數介紹
$("label[for='prize']").on('mouseover',function () {
	fundget_box_show();
	timer = setInterval(displayNextImage, 200);
	$('.prize-msg').show();
});
$("label[for='prize']").on('mouseleave',function () {
	$('#talk-box').hide();
	$('.prize-msg').hide();
	clearInterval(timer);
	$('#pork-guy-pic').attr("src","/static/img/pigman2.png");
});

//社福機構介紹
$("label[for='organizations']").on('mouseover',function () {
	fundget_box_show();
	timer = setInterval(displayNextImage, 200);
	$('.charity-msg').show()
	$('.charity-applied-pass-msg').hide();
	$('.charity-applied-nopass-msg').hide();
	$('.charity-noapplied-msg').hide();
});
$("label[for='organizations']").on('mouseleave',function () {
	$('#talk-box').hide();
	$('.charity-msg').hide();
	clearInterval(timer);
	$('#pork-guy-pic').attr("src","/static/img/pigman2.png");
});

//回饋金計畫申請未過的社福機構
$("label[for='applied-nopass']").on('mouseover',function () {
	fundget_box_show();
	timer = setInterval(displayNextImage, 200);
	$('.charity-applied-nopass-msg').show();
});
$("label[for='applied-nopass']").on('mouseleave',function () {
	$('#talk-box').hide();
	$('.charity-applied-nopass-msg').hide();
	clearInterval(timer);
	$('#pork-guy-pic').attr("src","/static/img/pigman2.png");
});

//申請通過的社福機構
$("label[for='applied-pass']").on('mouseover',function () {
	fundget_box_show();
	timer = setInterval(displayNextImage, 200);
	$('.charity-applied-pass-msg').show();
});
$("label[for='applied-pass']").on('mouseleave',function () {
	$('#talk-box').hide();
	$('.charity-applied-pass-msg').hide();
	clearInterval(timer);
	$('#pork-guy-pic').attr("src","/static/img/pigman2.png");
});

//未申請的社福機構
$("label[for='noapplied']").on('mouseover',function () {
	fundget_box_show();
	timer = setInterval(displayNextImage, 200);
	$('.charity-noapplied-msg').show();
});
$("label[for='noapplied']").on('mouseleave',function () {
	$('#talk-box').hide();
	$('.charity-noapplied-msg').hide();
	clearInterval(timer);
	$('#pork-guy-pic').attr("src","/static/img/pigman2.png");
});


//彩券行介紹
$("label[for='store']").on('mouseover',function () {
	fundget_box_show();
	$('#pork-guy-pic').attr("src","/static/img/pigtalk.gif");
	$('.prize-msg').show();
});
$("label[for='store']").on('mouseleave',function () {
	$('#talk-box').hide();
	$('.prize-msg').hide();
	$('#pork-guy-pic').attr("src","/static/img/pigman2.png");
});

$('#diagram').on('mouseover', function (){
	diagram_box_show();
	$('.explain').show();
});
$('#diagram').on('mouseleave', function (){
	$('#diagram-explain').hide();
	$('.explain').hide();
});

