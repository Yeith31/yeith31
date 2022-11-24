
marca=[]
modelo=[]
color=[]
combustible=[]
cilindraje=[]
precio=[]

tamaño=int(input("Tamaño de la lista?: "))

for i in range(tamaño):
    print("Ingrese los datos del vehiculo ",i+1)
    marcas=input("Marca del vehiculo ")
    modelos=input("Modelo del vehiculo ")
    colores=input("Color del vehiculo ")
    combustibles=input("Tipo de combustible ")
    cilindrajes=input("Cilindraje del vehiculo ")
    precios=input("Precio del vehiculo ")
    
    marca.append(marcas)
    modelo.append(modelos)
    color.append(colores)
    combustible.append(combustibles)
    cilindraje.append(cilindrajes)
    precio.append(precios)
    

print("-----------------------------------")
print("CONCESIONARIO YAS")
print("-------------------------------")
print("INFORMACION DEL VEHICULO ")
for i in range(tamaño):
    print("---------------------------------")
    print("---------------------------------")
    print("MARCA: ",marca[i])
    print("MODELO: ",modelo[i])
    print("COLOR: ",color[i])
    print("TIPO DE COMBUSTIBLE: ",combustible[i])
    print("CILINDRAJE: ",cilindraje[i])
    print("PRECIO $: ",precio[i])
    