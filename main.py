# main.py
from ui.ui_module import UI
from reduccion.reduccion_module import Reduccion

class Main:
    def __init__(self):
        self.minterms = []
        self.ui = UI()

    def ejecutar(self):
        # Mostrar el menú
        self.ui.mostrar_menu()

        # Pedir los minitérminos al usuario
        listaMinterminos = self.ui.ingresar_minterminos()

        # Se realiza una copia de la lista para calcular el número de variables que se requieren
        copiaListaMinterminos = listaMinterminos.copy()  # Hacemos una copia para futuras manipulaciones
        
        # Crear una instancia de la clase Reduccion con los minitérminos
        reduccion = Reduccion(listaMinterminos)  # Ahora listaMinterminos tiene los datos
        
        # Se obtiene el número de variables necesario del mayor número en la lista
        numeroVariables = reduccion.calcular_variables(copiaListaMinterminos)
       

if __name__ == "__main__":
    main = Main()
    main.ejecutar()
