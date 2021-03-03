
document.addEventListener('DOMContentLoaded',function(){
    let counter = 0 ;
    document.querySelector('#increase').onClick = function(){
        counter ++ ; 
        document.querySelector("h1").innerHTML = counter;
    } 
    document.querySelector("#decrease").onClick = function(){
        counter --;
        document.querySelector("h1").innerHTML = counter;
    }
})