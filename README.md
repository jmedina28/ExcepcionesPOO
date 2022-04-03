<h1 align="center">Excepciones</h1>

<h3 align="center">Autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
---
En este [repositorio](https://github.com/jmedina28/ExcepcionesPOO) quedan resueltos los ejercicios de excepciones para POO. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y de diversas fuentes que he encontrado.
***
## Ejercicio Excepciones

En este ejercicio he creado un programa el cual detecta si un correo electrónico esta escrito correctamente. También he introducido un límite de intentos cada cierto tiempo con el fin de evitar ciberataques.

El código que he desarrollado es el siguiente:

```python
import re
import time


class Login():

    def comprobacion(correo, tiempo, intentos):

        intentos += 1
        if intentos <= 5:

            if (re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", correo)):
                print("\nHa introducido su correo correctamente. Bienvenido:)")

            elif correo == "":
                print("Introduzca su correo electrónico por favor.")
                Login.comprobacion(
                    str(input("\nIntroduzca una dirección de correo electrónico correcta: ")), tiempo, intentos)
            else:
                print(
                    "Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")
                Login.comprobacion(
                    str(input("\nIntroduzca una dirección de correo electrónico: ")), tiempo, intentos)

        elif tiempo < 10:
            tiempo += 5
            print("\n---> Para evitar ciberataques usted no dispone de más intentos en los próximos " +
                  str(tiempo) + " segundos.")
            time.sleep(tiempo)
            Login.comprobacion(
                str(input("\nIntroduzca una dirección de correo electrónico: ")), tiempo, 0)
        else:
            print(
                "Usted ha agotado todas las oportunidades que tenía disponibles, vuelva a intentarlo más tarde.")


Login.comprobacion(
    str(input("Introduzca una dirección de correo electrónico: ")), 0, 0)
```
