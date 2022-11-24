var n;

n=parseInt(prompt("Digite un numero"))


//proceso

if (n >=10 && n<=100) {

    document.write("el numero "+n+" se encuentra entre 10 y 100 <img src='img/si2.png' height='35px'");
    
} else {
    
    document.write("el numero "+n+" NO se encuentra entre 10 y 100 <img src='img/no2.png' height='35px' ")
}