import re
correo = str(input("Introduzca una dirección de correo electrónico: "))

if (re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", correo)):
    print("Correo válido.")
else:
    print("Introduzca un correo electrónico válido por favor.")