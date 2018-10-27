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
          "4. Borrar serie:")
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


# Menu 1
def agregar():
    nuevaSerie = input("Ingrese la serie que desea agregar: ")
    series.append(nuevaSerie)
    print("Serie agregada exitosamente!\n")
    opcion = input("1. Agregar otra serie\n"
                   "9. Regresar\n"
                   "0. Salir\n"
                   ">>  ")
    exec_menu(opcion)
    return


# Menu 2
def mostrar():
    print(series)
    opcion = input("9. Regresar\n"
                   "0. Salir\n"
                   ">>  ")
    exec_menu(opcion)
    # print "Hello Menu 2 !\n"
    # print "9. Back"
    # print "0. Quit"
    # choice = raw_input(" >>  ")
    # exec_menu(choice)
    return


# Back to main menu
def back():
    acciones_menu['main_menu']()


# Exit program
def exit():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
acciones_menu = {
    'main_menu': main_menu,
    '1': agregar,
    '2': mostrar,
    '9': back,
    '0': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()