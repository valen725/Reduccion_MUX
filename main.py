# main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui.ui_module import UI
from GUI.gui_module import GUI  # El nuevo GUI basado en PyQt5
from reduccion.reduccion_module import Reduccion

class Main:
    def __init__(self):
        self.interface = None

    def seleccionar_interfaz(self):
        print("Selecciona la interfaz:")
        print("1. Interfaz de consola")
        print("2. Interfaz gráfica (GUI)")
        opcion = input("Ingresa el número de tu elección: ")

        if opcion == "1":
            self.interface = UI()
        elif opcion == "2":
            self.iniciar_gui()
        else:
            print("Opción no válida, usando interfaz de consola por defecto.")
            self.interface = UI()

    def iniciar_gui(self):
        # Inicializamos la GUI si el usuario la elige (PyQt5)
        app = QApplication(sys.argv)
        self.interface = GUI()  # Creamos la instancia de GUI
        self.interface.show()
        sys.exit(app.exec_())  # Ejecutamos el bucle principal de la GUI

    def ejecutar(self):
        # Seleccionar la interfaz
        self.seleccionar_interfaz()

        if isinstance(self.interface, UI):
            # Lógica para la interfaz de consola
            self.interface.mostrar_menu()

            lista_minterminos = self.interface.ingresar_minterminos()

            reduccion = Reduccion(lista_minterminos)
            numero_variables = reduccion.calcular_variables(lista_minterminos)

            tabla_verdad, num_bits = reduccion.crear_tabla_verdad()
            self.interface.imprimir_tabla_verdad(tabla_verdad, num_bits)

            self.interface.mostrar_num_entradas(numero_variables)

            numero_variables_selectoras,variable_control = reduccion.asignar_variable_control(numero_variables)
            self.interface.mostrar_variable_de_control(variable_control)
            self.interface.mostrar_variables_selectoras(numero_variables, numero_variables_selectoras)
            

            numero_entradas = reduccion.recalcular_entradas(numero_variables_selectoras)
            self.interface.mostrar_num_variables_reducidas(numero_entradas)

             # genera la tabla final
            tabla,columnas = reduccion.generar_tabla_mux(numero_variables)
            self.interface.imprimir_tabla(tabla, columnas)

            # Generar la tabla MUX con minterms marcados
            tabla_marcada, columnas, fila_A_negada_marcada, fila_A_marcada = reduccion.generar_tabla_mux_binarios(numero_variables)
            self.interface.imprimir_tabla(tabla_marcada, columnas)

            # Comparar columnas
            resultado = reduccion.comparar_columnas(fila_A_negada_marcada, fila_A_marcada)

            # Imprimir el resultado de la comparación sin tabla
            self.interface.imprimir_resultado(resultado)

if __name__ == "__main__":
    main = Main()
    main.ejecutar()
