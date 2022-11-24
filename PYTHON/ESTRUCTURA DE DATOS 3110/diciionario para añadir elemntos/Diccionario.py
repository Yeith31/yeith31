#Diseñe una app que permita ingresar al usaurio nombre,edad,direccion y telefono;estos 
# datos se deben almacenar en un diccionario llamado persona
#estos datos se deben mostar por pantalla de forma concatenada

#ejemplo
#juan tiene 17 años vive en la CLL 8 #27 18A y su numero de telefono es 1234567

nombre=input("Digite su nombre: ")
edad=input("Digite su edad ")
direccion=input("Digite su direccion ")
telefono=input("Digite su telefono ")

persona={"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}

print(persona["nombre"],"tiene ",persona["edad"],"años y vivve en ",persona["direccion"],"su numero de relefono es: ",persona["telefono"] )