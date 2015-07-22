// /*
// 	Spectral by HTML5 UP
// 	html5up.net | @n33co
// 	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
// */

// (function($) {

// 	skel
// 		.breakpoints({
// 			medium:	'(max-width: 980px)',
// 		});

// 	$(function() {

// 		var	$window = $(window),
// 			$body = $('body'),
// 			$wrapper = $('#page-wrapper'),
// 			$banner = $('#banner'),
// 			$header = $('#header');

// 		// Disable animations/transitions until the page has loaded.
// 			$body.addClass('is-loading');

// 			$window.on('load', function() {
// 				window.setTimeout(function() {
// 					$body.removeClass('is-loading');
// 				}, 100);
// 			});

// 		// Mobile?
// 			if (skel.vars.mobile)
// 				$body.addClass('is-mobile');
// 			else
// 				skel
// 					.on('-medium !medium', function() {
// 						$body.removeClass('is-mobile');
// 						$body.addClass('is-menu-visible');
// 					})    
// 					.on('+medium', function() {
// 						$body.addClass('is-mobile');
// 						$body.removeClass('is-menu-visible');
// 					});

// 		// Fix: Placeholder polyfill.
// 			$('form').placeholder();
// 		// Prioritize "important" elements on medium.
// 			skel.on('+medium -medium', function() {
// 				$.prioritize(
// 					'.important\\28 medium\\29',
// 					skel.breakpoint('medium').active
// 				);
// 			});

// 		// Scrolly.
// 			$('.scrolly')
// 				.scrolly({
// 					speed: 1500,
// 					offset: $header.outerHeight()
// 				});

// 		// Menu.
// 		// if($('.landing'))
// 		// 	$body.addClass('is-menu-visible');


// 		$window.on('resize',function() {
// 			if($('.is-mobile'))
// 			{
// 				$('#menu')
// 					.append('<a href="#menu" class="close"></a>')
// 					.appendTo($body)
// 					.panel({
// 						delay: 500,
// 						hideOnClick: true,
// 						hideOnSwipe: true,
// 						resetScroll: true,
// 						resetForms: true,
// 						side: 'right',
// 						target: $body,
// 						visibleClass: 'is-menu-visible'
// 					});
// 				$body.removeClass('is-menu-visible');
// 			}	
// 			else{
// 				body.addClass('is-menu-visible');
// 			}
// 		});
		
		

// 		// Header.
// 			if (skel.vars.IEVersion < 9)
// 				$header.removeClass('alt');

// 			if ($banner.length > 0
// 			&&	$header.hasClass('alt')) {

// 				$window.on('resize', function() { $window.trigger('scroll'); });

// 				$banner.scrollex({
// 					bottom:		$header.outerHeight() + 1,
// 					terminate:	function() { $header.removeClass('alt'); },
// 					enter:		function() { $header.addClass('alt'); },
// 					leave:		function() { $header.removeClass('alt'); }
// 				});

// 			}

// 	});

// })(jQuery);

		var	$window = $(window),
			$body = $('body'),
			$wrapper = $('#page-wrapper'),
			$banner = $('#banner'),
			$header = $('#header');

skel.breakpoints({
    medium: "(max-width: 980px)",
});



skel.on('-medium',function(){
	$body.addClass('is-menu-visible');
	$body.removeClass('is-menu-invisible');
	$('.close').remove();
	console.log(456)
})

skel.on('+medium',function(){
	//small
	$('#menu')
		.append('<a href="#menu" class="close" ></a>')
		.panel({
			delay: 500,
			hideOnClick: true,
			hideOnSwipe: true,
			resetScroll: true,
			resetForms: true,
			side: 'right',
			target: $body,
			visibleClass: 'is-menu-visible' 
		});
	$body.removeClass('is-menu-visible');
	$body.addClass('is-menu-invisible');	

	console.log(123)
});
$('.menuToggle').on('click',function(){	
	$body.removeClass('is-menu-invisible');
	$body.addClass('is-menu-visible');
	console.log("haha");
});



		// Scrolly.
			$('.scrolly')
				.scrolly({
					speed: 1500,
					offset: $header.outerHeight()
				});

		// Menu.
		// if($('.landing'))
		// 	$body.addClass('is-menu-visible');
		// Header.
			if (skel.vars.IEVersion < 9)
				$header.removeClass('alt');

			if ($banner.length > 0
			&&	$header.hasClass('alt')) {

				$window.on('resize', function() { $window.trigger('scroll'); });

				$banner.scrollex({
					bottom:		$header.outerHeight() + 1,
					terminate:	function() { $header.removeClass('alt'); },
					enter:		function() { $header.addClass('alt'); },
					leave:		function() { $header.removeClass('alt'); }
				});

			}