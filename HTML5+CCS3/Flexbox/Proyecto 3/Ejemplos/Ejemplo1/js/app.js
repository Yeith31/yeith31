//var es para definir las variables (definir/var)
var a,b,suma;

//escribir y leer con un solo comando para capturar los datos (prompt)
//(ParseInt, ParseFloat) para dconvertir una cadena de texto a entero o real

a=parseInt(prompt("Ingrese el 1er numero:"))
b=parseInt(prompt("Ingrese el 2do numero:"))


//proceso de la suma
suma=a+b;

//mensaje de salida (Document=write para solo escribir)
//(alert)mensaje de salida en forma de ventana emergente
//(console.log)
document.write("La suma de "+a+" + "+ b +" es igual a: "+suma);

