nombres=[]
DNI=[]
tamaño=int(input("Tamaño de la lista?: "))

for i in range(tamaño):
    print("Ingrese los datos del aprendiz ",i+1)
    nombre=input("Nombre del aprendiz ")
    id=input("Digite el numero de identificacion ")
    nombres.append(nombre)
    DNI.append(id)
print("Informacion del aprendiz ")
print("Los aprendices son ")
for i in range(tamaño):
    print("---------------------------------")
    print("nombre: ",nombres[i])
    print("Identificacion: ",DNI[i])