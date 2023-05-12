let bat_bar = new Array;
bat_bar=document.querySelectorAll('.bat');

bat_text = document.querySelectorAll(".progress-bar-text")

battery=new Array


const makebar = (percent, classname)=>{

    let i =0;
    let barFn = setInterval(function(){
        if(i<=percent){

            classname.style.width = i+"%"
            i++;
        }
        else{
            clearInterval(barFn);
        }

    }, 1);
}

for(let i=0; i<bat_bar.length;){
console.log(bat_text.innerText)
    battery[i]=bat_text[i].innerText.replace("%","")
    makebar(battery[i],bat_bar[i])
    i++
}