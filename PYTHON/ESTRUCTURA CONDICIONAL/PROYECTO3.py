#app que al ingresar la temperatura del paciente diga si este tiene fiebre o no

n=int(input("Digite la temperatura del paciente °"))

if n>37:
    print("El pacinete con la temperatura",n,"° tiene FIEBRE")
else:
    print("El pacinete con la temperatura",n,"° tiene temperatura normal")