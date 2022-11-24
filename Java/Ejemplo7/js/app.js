function sumar (){
    var x,y,z
    x=document.getElementById("n1").value
    y=document.getElementById("n2").value
    z=parseInt(x)+parseInt (y)
    
    document.getElementById("resultado_suma").innerHTML ="La suma es:" + z
    
}

function restar (){
    var x,y,z
    x=document.getElementById("n1").value
    y=document.getElementById("n2").value
    z=parseInt(x)-parseInt (y)
        
    document.getElementById("resultado_resta").innerHTML ="La resta es:" + z
        
}

function multi (){
    var x,y,z
    x=document.getElementById("n1").value
    y=document.getElementById("n2").value
    z=parseInt(x)*parseInt (y)
            
    document.getElementById("resultado_multi").innerHTML ="La multiplicacion es:" + z
            
}

function divi (){
    var x,y,z
    x=document.getElementById("n1").value
    y=document.getElementById("n2").value
    z=parseFloat(x)/parseFloat (y)

    document.getElementById("resultado_divi").innerHTML ="La divicion es:" + z
}
    


