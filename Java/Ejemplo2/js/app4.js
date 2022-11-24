var n;

n=parseFloat(prompt("Digite un numero del 1 al 5 para verificar si es primo"))

//proceso


if (n != 4) {

    document.write("El numero "+n+" es PRIMO <img src='img/si2.png' height='35px'");
    
} else {
    
    document.write("El numero "+n+" NO ES PRIMO <img src='img/no2.png' height='35px'");
}