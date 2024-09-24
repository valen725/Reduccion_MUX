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

    def mostrar_num_entradas(self,numero_variables):
        print("Numero de entradas iniciales del MUX: ", 2 ** numero_variables )

    
    def mostrar_variable_de_control(self,variable_control):
        print(f"\nLa variable de control asignada es: {variable_control}")

    def mostrar_variables_selectoras(self, numero_variables_iniciales, numero_variables_selectoras):
        # Muestra el número de variables iniciales y selectoras
        print(f"\nNúmero de variables selectoras iniciales: {numero_variables_iniciales}")
        print(f"Número de variables selectoras después de la reducción: {numero_variables_selectoras}")

    def mostrar_num_variables_reducidas(self,numero_entradas):
        print("Numero de entradas del MUX, luego, de realizar la reducción:  ",numero_entradas )

    def imprimir_tabla(self, tabla, columnas):
        print(tabulate(tabla, headers=[""] + columnas, tablefmt="grid"))

    def imprimir_resultado(self, resultado):
        # Imprimir el resultado sin formato de tabla, solo como una lista simple
        print("Resultado de la comparación de columnas:", resultado)