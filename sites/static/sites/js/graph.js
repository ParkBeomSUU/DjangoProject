const chart1 = document.querySelector('.doughnut1');
let battery = document.querySelector('.battery').innerHTML
const chart2 = document.querySelector('.doughnut2');
let l_rpm = document.querySelector('.l_rpm').innerHTML
const chart3 = document.querySelector('.doughnut3');
let r_rpm = document.querySelector('.r_rpm').innerHTML
battery = battery.replace("%","")


const makeChart = (percent, classname, color)=>{
    console.log("처음")
    let i =1;
    let chartFn= setInterval(function(){
        if(i<=percent){
            colorFn(i,classname, color);
            i++;
        }else{
            clearInterval(chartFn);
}
    }, 10);
}

const colorFn = (i, classname,color) =>{
    classname.style.background = "conic-gradient(" + color +" 0%" + i + "%, #dedede " + i + "% 100%)";
}

makeChart(battery,chart1,'#ff7f50')
makeChart(l_rpm,chart2,'#0A174E')
makeChart(l_rpm,chart3,'#87cefa')
