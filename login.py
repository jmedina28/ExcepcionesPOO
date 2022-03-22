import re
correo = str(input("Introduzca una dirección de correo electrónico: "))

def comprobacion(correo): 
    if (re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", correo)):
        return "Correo válido."
    elif correo == "":
        return "Introduzca su correo electrónico por favor."
    else:
        return "Una dirección de correo electrónico debe tener el formato xxx@xxx.xx"
    
print(comprobacion(correo))