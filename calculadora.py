"""
a- Ingreso un operando
b- Ingreso segundo operando
c- Operaciones
d- Mostrar Resultado
e- Salir

Se van desbloqueando cuando el anterior se realizo
Una ver Mostrado el resultado se bloquea todo de nuevo
Lo unico no bloqueado es el punto a y e al inicio
Cuidado con el erro de dividir por 0
"""
from funciones_operadores import *

primer_paso = False
segundo_paso = False
tercer_paso = False
numero_uno = None
numero_dos = None

def menu():
    v1_str = f"V1 = {numero_uno}" if numero_uno is not None else "V1 no ingresado"
    v2_str = f"V2 = {numero_dos}" if numero_dos is not None else "V2 no ingresado"

    print(f'''\na- Ingresar primer valor   {v1_str}
b- Ingresar segundo valor   {v2_str}
c- Operaciones
d- Mostrar Resultado
e- Salir\n''')
    return input("\nSeleccione una opcion del menu : \n")

while True:
    match menu():
        case "a":
            numero_uno = ingresar_validar_numero()
            primer_paso = True
        case "b":
            if primer_paso:
                numero_dos = ingresar_validar_numero()
                segundo_paso = True
            else:
                print("\nDebe ingresar el primer valor\n")
        case "c":
            if segundo_paso:
                menuOperaciones()
                resultado = whileOpciones(numero_uno,numero_dos)
                tercer_paso = True
            else:
                print("\nDebe ingresar ambos valores\n")
        case "d":
            if tercer_paso:
                print(resultado)
                primer_paso = False
                segundo_paso = False
                tercer_paso = False
            elif segundo_paso:
                print("\nNo podes ver el resultado sin ingresar un operador\n")
            else:
                print("\nDebe ingresar ambos valores\n")
        case "e":
            break
