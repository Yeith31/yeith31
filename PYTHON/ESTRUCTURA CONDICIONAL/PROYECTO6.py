#app que al ingresar un valor de ingrso y un valor de gastos diga si son ganancias o perdidas

n1=int(input("Digite el valor de ingreso "))
n2=int(input("Digite el valor de gastos "))

if n1>n2:
    print("El ingreso de ",n1," COP se convirtieron en GANANCIAS")
else:
    print("El ingreso de ",n1," COP se convirtieron en PERDIDAS")