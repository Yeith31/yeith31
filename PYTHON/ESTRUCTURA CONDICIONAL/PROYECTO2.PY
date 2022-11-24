#app que al ingresar el valor de compra 
# si la compra es mayor a $100k, entonces calcule(7%) el descuento y el total de la compra

valor_compra=float(input("Digite el valor total de la compra ")) 

if valor_compra>100000:
    descuento=valor_compra*0.07
    tt=valor_compra-descuento
    print("SUBTOTAL:",valor_compra,)
    print("DESCUENTO:",descuento,)
    print("TOTAL:",tt,)
else:
    descuento=valor_compra*0.00
    tt=valor_compra-descuento
    print("SUBTOTAL:",valor_compra,)
    print("DESCUENTO:",descuento,)
    print("TOTAL:",tt,)