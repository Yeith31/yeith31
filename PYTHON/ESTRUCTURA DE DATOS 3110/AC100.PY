nombres=[]
DNI=[]
correo=[]
cel=[]
dire=[]
lugar=[]
fecha=[]

tamaño=int(input("Tamaño de la lista?: "))

for i in range(tamaño):
    print("Ingrese los datos del aprendiz ",i+1)
    nombre=input("Nombre del aprendiz ")
    id=input("Digite el numero de identificacion ")
    mail=input("Digite su correo electronico ")
    Num=input("Digite su numero de telefono ")
    calle=input("Digite su direccion de recidencia ")
    lugna=input("Digite su lugar de nacimiento ")
    fnaci=input("Digite su fecha de nacimiento ")

    nombres.append(nombre)
    DNI.append(id)
    correo.append(mail)
    dire.append(calle)
    lugar.append(lugna)
    fecha.append(fnaci)
print("-----------------------------------")
print("-------------------------------")
print("INFORMACION DEL APRENDIZ9 ")
for i in range(tamaño):
    print("---------------------------------")
    print("---------------------------------")
    print("nombre: ",nombres[i])
    print("Identificacion: ",DNI[i])
    print("Correo electronico: ",correo[i])
    print("N° de celular: ",cel[i])
    print("Direccion de recidencia: ",dire[i])
    print("Lugar de nacimiento: ",lugar[i])
    print("Fecha de nacimiento: ",fecha[i])