nombres=[]
tamaño=int(input("Tamaño de la lista?: "))

for i in range(tamaño):
    print("Ingrese los datos del aprendiz ",i+1)
    nombre=input("Nombre del aprendiz ")
    nombres.append(nombre)
print("Los aprendices son ")
for i in range(tamaño):
    print("---------------------------------")
    print("nombre: ",nombres[i])
