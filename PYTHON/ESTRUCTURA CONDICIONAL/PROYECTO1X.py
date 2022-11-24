#app que al ingresar una edad diga si es baby mayor joben etc.
#0> Y <2=eres un baby
#2> y <12=eres un niño
#12> y <17=eres un adolecente
#18> y<40 eres un adulto joven
#40> y <60 eres un adulto maduro
#>60 eres un adulto mayor

n=int(input("Digite la edad "))

if n>=0 and n<2:
    print("ERES UN BABBY")
elif n>=2 and n<12:
    print("ERES UN NIÑ@")
elif n>=12 and n<18:
    print("ERES UN ADOLECENTE")
elif n>=18 and n<40:
    print("ERES UN ADULTO JOVEN")
elif n>=40 and n<60:
    print("ERES UN ADULTO MADURO")
elif n>=60:
    print("ERES UN ADULTO MAYOR")
else:
    print("DIGITE SU EDAD CORRECTAMENTE")