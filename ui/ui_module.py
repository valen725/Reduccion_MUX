from tabulate import tabulate
import string

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
    
    def imprimir_tabla_verdad(self,tabla,num_bits):
         # Generar los encabezados usando las primeras letras del alfabeto (A, B, C, ...)
        headers = list(string.ascii_uppercase[:num_bits]) + ['Salida']  # 'A', 'B', 'C', etc.
        # Imprimir la tabla usando la librería tabulate
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
