


codigoc=[]
codigof=[]
nombrec=[]
fecha=[]
descr=[]
preciou=[]
cantidad=[]
totall=[]


tamaño=int(input("Tamaño de la lista?: "))

for i in range(tamaño):
    print("Ingrese los datos de la factura ",i+1)
    codic=input("CODIGO DE CLIENTE ")
    codif=input("CODIGO DE FACTURA: ")
    namec=input("NOMBRE DEL CLIENTE: ")
    fechaa=input("FECHA DE FACTURACION: ")
    desp=input("DESCRIPCION DEL PRODUCTO: ")
    preciu=int(input("PRECIO: "))
    canti=int(input("CANTIDAD: "))
    
    


    codigoc.append(codic)
    codigof.append(codif)
    nombrec.append(namec)
    fecha.append(fechaa)
    descr.append(desp)
    preciou.append(preciu)
    cantidad.append(canti)
    totall.append(preciu*canti)
       


print("-----------------------------------")
print("TIENDAS MANOLO S.A.S")
print("-------------------------------")
print("FACTURA DE VENTA  ")
for i in range(tamaño):
    print("---------------------------------")
    print("---------------------------------")
    print("CODIGO DEL CLIENTE: ",codigof[i])
    print("CODIGO DE FACTURA: ",codigof[i])
    print("NOMBRE DEL CLIENTE: ",nombrec[i])
    print("FECHA: ",fecha[i])
    print("DESCRIPCION DEL PRODUCTO: ",descr[i])
    print("PRECIO $: ",preciou[i])
    print("CANTIDAD: ",cantidad[i])
    print("TOTAL $: ",totall[i])
    