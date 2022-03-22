import re
import time

class Login():

    def comprobacion(correo, tiempo, intentos):

        intentos += 1
        if intentos <= 5:

            if (re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", correo)):
                print("Ha introducido su correo correctamente. Bienvenido:)")

            elif correo == "":
                print("Introduzca su correo electrónico por favor.")
                Login.comprobacion(
                    str(input("Introduzca una dirección de correo electrónico correcta: ")), tiempo, intentos)
            else:
                print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
                Login.comprobacion(
                    str(input("Introduzca una dirección de correo electrónico: ")), tiempo, intentos)

        elif tiempo < 10:
            tiempo += 5
            print("Para evitar ciberataques usted no dispone de más intentos en los próximos " +
                str(tiempo) + " segundos.")
            time.sleep(tiempo)
            Login.comprobacion(
                str(input("Introduzca una dirección de correo electrónico: ")), tiempo, 0)
        else:
            print("Usted ha agotado todas las oportunidades que tenía disponibles, vuelva a intentarlo más tarde.")


Login.comprobacion(
        str(input("Introduzca una dirección de correo electrónico: ")), 0, 0)
