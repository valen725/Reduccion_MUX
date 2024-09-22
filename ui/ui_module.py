class UI:
    def mostrar_menu(self):
        print("\t╔══════════════════════════════════════════════════╗")
        print("\t║                    REDUCCIÓN MUX                 ║")
        print("\t╚══════════════════════════════════════════════════╝\n")

    def ingresar_minterminos(self):
        # Solicitar entrada al usuario usando comas como separadores
        minTerminos = input("Ingrese los mintérminos separados por comas -> Ej. 1,4,6,7,8,9: ")
        # Dividir la cadena de entrada en función de las comas
        lista_minterminos = sorted(list(map(int, minTerminos.split(',')))) # Convertir a enteros y organizar la lista de menor a mayor
        return lista_minterminos

