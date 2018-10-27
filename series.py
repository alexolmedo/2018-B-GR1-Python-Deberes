import sys, os

# Definicion de constantes de menu
acciones_menu = {}

# Arreglo de series

series = []

# Menu principal
def main_menu():
    os.system('cls')
    print("TV SERIES\n"
          "Elija una opcion para comenzar:\n"
          "1. Agregar serie\n"
          "2. Mostrar series\n"
          "3. Actualizar serie\n"
          "4. Borrar serie\n"
          "x. Salir\n"
          )
    opcion= input("Opcion seleccionada >> ")
    exec_menu(opcion)
    return

# Ejecutar menu
def exec_menu(opcion):
    os.system('cls')
    ch = opcion.lower()
    if ch == '':
        acciones_menu['main_menu']()
    else:
        try:
            acciones_menu[ch]()
        except KeyError:
            print("Seleccion inválida, intente de nuevo\n")
            acciones_menu['main_menu']()
    return


# Agregar Serie
def agregar():
    nuevaSerie = input("Ingrese la serie que desea agregar: ")
    series.append(nuevaSerie)
    print("Serie agregada exitosamente!\n")
    opcion = input("1. Agregar otra serie\n"
                   "r. Regresar\n"
                   "x. Salir\n"
                   ">>  ")
    exec_menu(opcion)
    return


# Mostrar series
def mostrar():
    imprimirSeries()
    opcion = input("\nr. Regresar\n"
                   "x. Salir\n"
                   ">>  ")
    exec_menu(opcion)
    return

# Actualizar serie
def actualizar():
    imprimirSeries()
    opcion = input("\nr. Regresar\n"
                   "x. Salir\n"
                   ">>  ")
    exec_menu(opcion)
    return

# Borrar serie
def borrar():
    imprimirSeries()
    indiceSerieBorrada = input("Seleccione la serie que desea borrar: ")
    series.pop(int(indiceSerieBorrada)-1)
    os.system('cls')
    print("Serie borrada exitosamente!")
    imprimirSeries()
    opcion = input("\nb. Borrar otra serie\n"
                   "r. Regresar\n"
                   "x. Salir\n"
                   ">>  ")
    exec_menu(opcion)
    return

def imprimirSeries():
    indice = 1
    for item in series:
        print(str(indice) + ". " + item)
        indice += 1

# Volver al menu principal
def back():
    acciones_menu['main_menu']()


# Salir del programa
def exit():
    sys.exit()

# Definiciones del menu
acciones_menu = {
    'main_menu': main_menu,
    '1': agregar,
    '2': mostrar,
    'b': borrar,
    '3': actualizar,
    '4': borrar,
    'r': back,
    'x': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()