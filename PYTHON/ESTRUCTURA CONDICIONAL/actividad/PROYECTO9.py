n1=int(input("Digite la cantidad de pares de zapatos "))
n2=float(input("Digite el precio del par de Zapatos "))

if n1<10:
    
    print("No tiene ningun descuento")

elif n1>=10 and n1<=20:
    t=n1*n2
    des=n2*0.10
    tt=t-des
    print("el total de su compra es de",t," y tiene un 10% de descuento en su compra el cual es: ",des)
    print("Su total en la compra es de",tt)
elif n1>=20 and n1<=30:
    t=n1*n2
    des=n2*0.20
    tt=n2-des
    print("el total de su compra es de",t," y tiene un 20% de descuento en su compra el cual es: ",des)
    print("Su total en la compra es de",tt)   
elif n1>30:
    t=n1*n2
    des=n2*0.40
    tt=n2-des
    print("el total de su compra es de",t," y tiene un 40% de descuento en su compra el cual es: ",des)
    print("Su total en la compra es de",tt)   
else:
    print("******ERROR DESCONOCIDO******")   
        