import re
import time 

correo = str(input("Introduzca una dirección de correo electrónico: "))
tiempo = 0
intentos = 0

def comprobacion(correo,tiempo,intentos): 
    
    intentos += 1
    if intentos <= 10:    
        if (re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", correo)):
            print("Correo válido. Bienvenido:)")
            
        elif correo == "" or correo == " ":
            print("Introduzca su correo electrónico por favor.")
            comprobacion(str(input("Introduzca una dirección de correo electrónico: ")), tiempo, intentos)
        else:
            print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
            comprobacion(str(input("Introduzca una dirección de correo electrónico: ")), tiempo, intentos)
    else:
        tiempo += 8
        print("Para evitar ciberataques usted no dispone de más intentos en los próximos " + str(tiempo) + " segundos")
        time.sleep(tiempo)
        comprobacion(str(input("Introduzca una dirección de correo electrónico: ")), tiempo, intentos)
            
        
comprobacion(correo,tiempo,intentos)