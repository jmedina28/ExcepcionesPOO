import re
import time 

correo = str(input("Introduzca una dirección de correo electrónico: "))
tiempo, intentos = 0, 0

def comprobacion(correo,tiempo,intentos): 
    

    if intentos <= 5:    
        intentos += 1
        if (re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", correo)):
            print("Correo válido. Bienvenido:)")
            
        elif correo == "":
            print("Introduzca su correo electrónico por favor.")
            comprobacion(str(input("Introduzca una dirección de correo electrónico: ")),tiempo,intentos)
        else:
            print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
            comprobacion(str(input("Introduzca una dirección de correo electrónico: ")),tiempo,intentos)
    elif tiempo <=15:
        tiempo += 5
        print("Para evitar ciberataques usted no dispone de más intentos en los próximos " + str(tiempo) + " segundos")
        time.sleep(tiempo) 
        comprobacion(str(input("Introduzca una dirección de correo electrónico: ")),tiempo,0)
    else:
        print("Usted ha agotado todas las oportunidades que tenía disponibles, vuelva a intentarlo más tarde.")
            
        
comprobacion(correo,tiempo,intentos)