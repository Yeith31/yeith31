
var temp;

temp=parseFloat(prompt("Ingrese su temperatura en °C:"));


//proceso para evaluar la fiebre

if (temp >=38 ) {

    document.write("La temperatura de "+temp+" indica que el paciente tiene fiebre");
    
} else {
    
    document.write("La temperatura de "+temp+" es normal(no tiene fiebre)");
}