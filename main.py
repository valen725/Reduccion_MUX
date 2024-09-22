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
        self.minterms = self.ui.ingresar_minterminos()

        # Crear una instancia de la clase Reduccion con los minitérminos
        reduccion = Reduccion(self.minterms)

        # Mostrar la tabla con los minitérminos y sus representaciones binarias
        reduccion.mostrar_tabla()

if __name__ == "__main__":
    main = Main()
    main.ejecutar()

