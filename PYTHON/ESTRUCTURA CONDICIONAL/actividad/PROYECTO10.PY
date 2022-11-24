n=int(input("Digite su precion arterial "))

if n<90:
    print( "la precion arterial del paciente es BAJA")
elif n<120:
    print("la precion arterial del paciente es BAJA")    
elif n>=120 and n<=139:
    print("la precion arterial del paciente es PREHIPERTENSION")
elif n>=140 and n<=159:
    print("la precion arterial del paciente es ALTA: HIPERTENSION FASE 1")
elif n>=160:
    print("la precion arterial del paciente es ALTA: HIPERTENSION FASE 2")
else:
    print("***** ERROR DESCONOCIDO*****")