import re
correo = str(input("Introduzca una dirección de correo electrónico: "))

def comprobacion(correo): 
    intentos = 0
    tiempo = 0
    while True:
        intentos += 1
        if intentos <= 10:    
            if (re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", correo)):
                print("Correo válido.")
                break
            elif correo == "":
                print("Introduzca su correo electrónico por favor.")
                correo = str(input("Introduzca una dirección de correo electrónico: "))
            else:
                print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
                correo = str(input("Introduzca una dirección de correo electrónico: "))
        else:
            print("Para evitar ciberataques usted no dispone de más intentos en los próximos " + str(tiempo) + " segundos")
            break
        
comprobacion(correo)