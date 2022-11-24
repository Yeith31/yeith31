#diseñe una app que permita al usuario ingrear frutas y el precio unitario y la cantidad  y lo almacene en un diccionario llamado factura. 
#despues debe mostar un mensaje concatenado
#donde aparece el nombre de la fruta su valor la cantidad y el total

frutas=input("Digte el nombre de su fruta ")
preciou=int(input("Digite el precio unitario "))
cantidad=int(input("Digite la cantidad de frutas "))



factura={"frutas":frutas,"preciou":preciou}

print("Su",factura["frutas"],"tiene un valor unitario de ",factura["preciou"],"y su total de la compra es: ",(cantidad*preciou))