$(function(){
	$(".main-visual-slide").bxSlider({
		auto:true, //자동으로 애니메이션 시작
		pause:2000, //유지시간 2초
		autoHover:true,
		autoControls:true,
		autoControlsCombine:true
	});

	$("#notice-tab-wrap h4 a").on("click", tabmenu);
	function tabmenu(e) {
		e.preventDefault();
		var $ts = $(this);
		var $next = $ts.parent().next();
		if($next.is(":hidden")){
			$("#notice-tab-wrap h4 a").removeClass("on");
			$ts.addClass("on");
			$("#notice-tab-wrap > div:visible").hide();
			$next.show();
		}
	}


 
});