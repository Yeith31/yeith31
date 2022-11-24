var n;

n=parseFloat(prompt("Digite la nota"))

//proceso


if (n >=0 && n>=3) {

    document.write("la asigantura con la nota "+n+" esta APROBADA <img src='img/si2.png' height='35px'");
    
} else {
    
    document.write("la asigantura con la nota "+n+" esta REPROBADA <img src='img/no2.png' height='35px'");
}