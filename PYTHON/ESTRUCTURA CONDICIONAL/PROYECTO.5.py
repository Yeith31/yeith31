#app que al ingresar una nota del estudiante diga si esta es APROBADA o REPROBADA

n=float(input("Digite la nota del estudiante "))

if n>2.9:
    print("El nota", n ,"es APROBADA")
else:
    print("La nota", n ,"es REPROBADA")