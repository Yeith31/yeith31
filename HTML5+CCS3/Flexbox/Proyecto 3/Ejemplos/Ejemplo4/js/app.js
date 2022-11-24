var peso,estatura;
var imc;

peso=parseFloat(prompt("Digite su peso en KG"))
estatura=parseFloat(prompt("Digite su estatura en M"))


imc=peso/(estatura*estatura)

if (imc < 18.5) {

    document.write("Su IMC es "+imc+" equivalente a un PESO BAJO")

}else if(imc >= 18.5 && imc <=24.9){

    document.write("Su IMC es "+imc+" equivalente a un PESO NORMAL")

}else if(imc >= 25 && imc <=29.9){
    document.write("Su IMC es "+imc+" equivalente a un SOBREPESO")

}else if(imc >= 30 && imc <=34.9){
    document.write("Su IMC es "+imc+" equivalente a un OBESIDAD I")

}else if(imc >= 35 && imc <=39.9){
    document.write("Su IMC es "+imc+" equivalente a un OBESIDAD II")

}else if(imc >= 40 && imc <=49.9){
    document.write("Su IMC es "+imc+" equivalente a un OBESIDAD III")

}else if(imc >= 50){
    document.write("Su IMC es "+imc+" equivalente a un OBESIDAD VI")

}else{

    document.write("Digite los valores numericos esperados............")
} 
