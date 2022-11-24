
var op;
var n1,n2,resultado;

op=parseInt(prompt("<<<<CALCULADORA 3.0>>>>\nEliga una opcion del menu \n 1.SUMA \n 2.RESTA \n 3.MULTIPLICACION \n 4.DIVICION"))

switch (op) {
    case 1:
        n1=parseInt(prompt("Digite el 1er nunero"))
        n2=parseInt(prompt("Digite el 2do nunero"))
        resultado=n1+n2;
        document.write("La suma de "+n1+" + " +n2+" es:"+resultado)

    break;

    case 2:
        n1=parseInt(prompt("Digite el 1er nunero"))
        n2=parseInt(prompt("Digite el 2do nunero"))
        resultado=n1-n2;
        document.write("La resta de "+n1+" - " +n2+" es:"+resultado)

    break;

    case 3:
        n1=parseInt(prompt("Digite el 1er nunero"))
        n2=parseInt(prompt("Digite el 2do nunero"))
        resultado=n1*n2;
        document.write("La multiplicacion de "+n1+" * " +n2+" es:"+resultado)

    break;

    case 4:
        n1=parseFloat(prompt("Digite el 1er nunero"))
        n2=parseFloat(prompt("Digite el 2do nunero"))
        resultado=n1/n2;
        document.write("La divicion de "+n1+" / " +n2+" es:"+resultado)

    break;

    default:

    document.write("Seleccione una opcion del menu")

    break;

}