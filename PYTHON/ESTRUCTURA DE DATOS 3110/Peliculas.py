
titulo=[]
ano=[]
genero=[]
duracionpel=[]
protagonista=[]
precio=[]
idioma=[]

tamaño=int(input("Tamaño de la lista?: "))

for i in range(tamaño):
    print("Ingrese los datos del vehiculo ",i+1)
    titulos=input("TITULO DE LA PLEICULA ")
    gene=input("GENERO: ")
    dura=input("DURACION: ")
    prota=input("PROTAGONISTA DE LA PELICULA: ")
    anos=input("AÑO DE ESTRENO: ")
    precios=input("PRECIO: ")
    idiomas=input("IDIOMA: ")
    
    titulo.append(titulos)
    genero.append(gene)
    duracionpel.append(dura)
    protagonista.append(prota)
    precio.append(precios)
    idioma.append(idiomas)
    

print("-----------------------------------")
print("SERIESFLIX")
print("-------------------------------")
print("INFORMACION DE LA PELICULA ")
for i in range(tamaño):
    print("---------------------------------")
    print("---------------------------------")
    print("TITULO DE LA PELICULA: ",titulo[i])
    print("GENERO: ",genero[i])
    print("DURACION: ",duracionpel[i])
    print("PROTAGONISTA: ",protagonista[i])
    print("PRECIO $: ",precio[i])
    print("IDIOMA: ",idioma[i])
    