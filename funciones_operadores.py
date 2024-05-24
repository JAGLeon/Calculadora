def ingresar_validar_numero()-> int:
    numero = input("Ingrese un numero : ")
    while not numero.isdigit():
        numero = input("ERROR re-ingrese un numero : ")
    return int(numero)

def numero_distinto_a_cero():
    numero = ingresar_validar_numero()
    while numero == 0:
        print("Por favor, ingrese un valor distinto a 0")
        numero = ingresar_validar_numero()
    return numero

def suma(valor_uno: int, valor_dos: int)-> int:
    return valor_uno + valor_dos

def resta(valor_uno: int, valor_dos: int)-> int:
    return valor_uno - valor_dos

def dividir(valor_uno: int, valor_dos: int)-> float:
    return valor_uno / valor_dos

def multiplicar(valor_uno: int, valor_dos: int)-> int:
    return valor_uno * valor_dos

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

def menuOperaciones():
    print('''\n1- Sumar
2- Restar
3- Dividir
4- Multiplicar
5- Factorial\n''')
    return

def whileOpciones(valor_uno: int, valor_dos: int):
    while True:
        opcion = input("\nIngrese un opcion : \n")
        match opcion.lower():
            case "sumar" | "1":
                return f"\nEl resultado de {valor_uno}+{valor_dos} es: {suma(valor_uno,valor_dos)}\n" 
            case "restar" | "2":
                return f"\nEl resultado de {valor_uno}-{valor_dos} es: {resta(valor_uno,valor_dos)}\n" 
            case "dividir" | "3":
                if valor_dos == 0:
                    respuesta = input("No se puede dividir por 0\n¿Desea cambiar el 2do valor? [Y/N]\n")
                    if respuesta.lower() == "y":
                        valor_dos = numero_distinto_a_cero()
                        return f"\nEl resultado de {valor_uno}/{valor_dos} es: {dividir(valor_uno,valor_dos)}\n" 
                    else:
                        return "\nNo se puede dividir por 0\n"
                else:
                    return f"\nEl resultado de {valor_uno}/{valor_dos} es: {dividir(valor_uno,valor_dos)}\n" 
            case "multiplicar" | "4":
                return f"\nEl resultado de {valor_uno}*{valor_dos} es: {multiplicar(valor_uno,valor_dos)}\n" 
            case "factorial" | "5":
                return f"\nEl factorial de {valor_uno} es: {factorial(valor_uno)} y El factorial de {valor_dos} es: {factorial(valor_dos)}\n"


