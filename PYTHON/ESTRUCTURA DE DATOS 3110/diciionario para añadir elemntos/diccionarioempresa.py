
cliente={}
op=""

while op !=4:
    if op ==1:
        id=input("Digite su identificacion ")
        nombre=input("Digite su nombre ")
        direccion=input("Digte su direccion ")
        telefono=input("Digite su telefono ")
        correo=input("Digite su correo")
        empresa=input("Digite el nombre de su empresa")

        clientes={
            "id":id,
            "nombre":nombre,
            "direccion":direccion,
            "telefono":telefono,
            "correo":correo,
            "empresa":empresa
        }
        

    if op ==2:
        print("-----INFORMACION CLIENTES------")
        print("-----------------------------------")
        print(clientes["nombre"],"Identicidado con el numero",clientes["id"],"con recidencia en",clientes["direccion"],",con numero de telefono",clientes["telefono"],",con el correo",clientes["correo"],"de la empresa",clientes["empresa"])
        
    if op==3:
        del[id]
        print("---------------------------------")
        print("CLIENTE ELIMINADO CON EXITO!!")


    if op==4:
        exit()

        
    print("--------MENU---------")
    print("1-AÑADIR CLIENTE")
    print("2-MOSTRAR CLIENTE")
    print("3-ELIMINAR CLIENTE")
    print("4-SALIR")
    op=int(input("Digite la opcion seleccionada: "))
