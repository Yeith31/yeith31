peso=float(input("Digite su peso en KG " ))
estatura=float(input("Digite su estatura en M "))

imc=peso/(estatura*estatura)

if imc < 18.5:
 print("Su IMC es ",imc," equivalente a un PESO BAJO")

elif imc >= 18.5 and imc <= 24.9:
 print("Su IMC es ",imc," equivalente a un PESO NORMAL")

elif imc >= 25 and imc <= 29.9:
 print("Su IMC es ",imc," equivalente a un SOBREPESO")

elif imc >= 30 and imc <= 34.9:
 print("Su IMC es ",imc," equivalente a un OBESIDAD I")

elif imc >= 35 and imc <= 39.9:
 print("Su IMC es ",imc," equivalente a un OBESIDAD II")

elif imc >= 40 and imc <= 49.9:
 print("Su IMC es ",imc," equivalente a un OBESIDAD III")

elif imc >= 50:
 print("Su IMC es ",imc," equivalente a un OBESIDAD VI")

else:
   print("Digite los valores numericos esperados............")
