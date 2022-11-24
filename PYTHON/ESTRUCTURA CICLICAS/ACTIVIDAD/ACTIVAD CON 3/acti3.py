#APP QUE MUESTRE LOS NUMEROS IMPARES (DESDE,HASTA) INGRESADOS POR EL USUARIO
from re import X


x=int(input("DIGITE UN NUMERO POSITIVO "))
for i in range(1, x+1, 2):
    print(i, end=", ")