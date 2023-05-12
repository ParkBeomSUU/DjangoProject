// 처음실행 부분
$('document').ready(function(){
    //배터리 부분 
    let chart1=$('.doughnut1')
    // console.log("chart부분",chart1)
    let battery=$('.battery').text()
    // console.log("배터리",battery)
    battery=battery.replace("%","")
    // console.log(battery)
    const makeChart = (percent, classname)=>{
        // console.log("처음")
        let i =1;
        let chartFn= setInterval(function(){
            
            if(i<=percent){
                if(percent>=60){
                    color="#4cd964"
                    colorFn(i,classname,color)
                    i++
                }
                else if(percent>30){
                    color="#ffcc00"
                    colorFn(i,classname,color)
                    i++
                }
                else{
                    color="#ff0000"
                    colorFn(i,classname,color)
                    i++
                }
            }
            else{
                clearInterval(chartFn);
    }
        }, 15);
    }
    
    const colorFn = (i, classname,color) =>{
        classname.css("background","conic-gradient(" + color +" 0%" + i + "%, #dedede " + i + "% 100%)");
    }


    makeChart(battery,chart1)

})

//onclick 이벤트부분(배터리)

function barchange(num){
    //배터리부분
    var battery =$('#bat').val()
    var chart1=$('.doughnut1')
    // console.log(battery)
    //RGB부분
    var rgb=$('.child1')
    var r=$('.child2')
    var g=$('.child3')
    var b=$('.child4')

    var r_led =$('#r_led').val()
    var g_led =$('#g_led').val()
    var b_led =$('#b_led').val()
    // console.log(r_led, g_led, b_led)
    
    //엔코더부분
    var r_rpm =$('#r_rpm').val()
    var l_rpm =$('#l_rpm').val()

    
    $.ajax({ 
        url: num ,    //request 보낼 서버의 경로
        type:'post', // 메소드(get, post, put 등)
        data:JSON.stringify({'battery': battery,
                             'r_led': r_led,
                             'g_led': g_led,
                             'b_led': b_led,
                             'r_rpm': r_rpm,
                             'l_rpm': l_rpm,}), //보낼 데이터
        success: function(context){
        // console.log("전송 성공")
        if(num==1){ 
            console.log("Bat start") 
            bat=context.battery
            // console.log("bat",bat)
            const makeChart = (percent, classname)=>{
                // console.log("처음")
                let i =1;
                let chartFn= setInterval(function(){
                    
                    if(i<=percent){
                        if(percent>=60){
                            color="#4cd964"
                            colorFn(i,classname,color)
                            i++
                        }
                        else if(percent>=30){
                            color="#ffcc00"
                            colorFn(i,classname,color)
                            i++
                        }
                        else{
                            color="#ff0000"
                            colorFn(i,classname,color)
                            i++
                        }
                    }
                    else{
                        clearInterval(chartFn);
            }
                }, 15);
                
                console.log(typeof(bat))
                $('.battery').text(bat+"%")
            }
            
            const colorFn = (i, classname,color) =>{
                classname.css("background","conic-gradient(" + color +" 0%" + i + "%, #dedede " + i + "% 100%)");
            }
            makeChart(bat,chart1)
            
        }
        // RGB
        if(num==2){
            console.log("RGB start") 
            r_led=parseInt(context.r_led)
            g_led=parseInt(context.g_led)
            b_led=parseInt(context.b_led)
            
            r.css("background-color", `rgb(${r_led},0,0)`);
            g.css("background-color", `rgb(0,${g_led},0)`);
            b.css("background-color", `rgb(0,0,${b_led})`);
            rgb.css("background-color", `rgb(${r_led},${g_led},${b_led})`);
        }

        if(num==3){
            // console.log("Encoder start")
            r_rpm=parseInt(context.r_rpm)
            l_rpm=parseInt(context.l_rpm)
            // console.log("시작전 r:",r_rpm,"l:",l_rpm) 

            if(r_rpm<10){
                r_rpm=parseInt(10-context.r_rpm)
            }
            else if(r_rpm<100){
                r_rpm=parseFloat((1/r_rpm)*40+0.02).toFixed(4)
            }

            else if(r_rpm>=100){
                r_rpm=parseFloat((1/r_rpm)*40+0.02).toFixed(4)
            }

            if(l_rpm<10){
                l_rpm=parseInt(10-context.l_rpm)
            }
            else if(l_rpm<100){
                l_rpm=parseFloat((1/l_rpm)*40+0.02).toFixed(4)
            }

            else if(l_rpm>=100){
                l_rpm=parseFloat((1/l_rpm)*40+0.02).toFixed(4)
            }
            
            // console.log("시작후 r:",r_rpm,"l:",l_rpm)
 
            
            const tireRTag = document.querySelector(".r_tire > img");
            const tireLTag = document.querySelector(".l_tire > img");

            tireRTag.style.animation = "rotate_image "+r_rpm+"s linear infinite";
            tireRTag.style.transformOrigin = "50% 50%";

            tireLTag.style.animation = "rotate_image "+l_rpm+"s linear infinite";
            tireLTag.style.transformOrigin = "50% 50%";


              
            

            
        }
    }
})

}
