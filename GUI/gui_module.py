from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QTextEdit, QVBoxLayout, QLabel, QWidget
from PyQt5 import QtWidgets
from reduccion.reduccion_module import Reduccion
import string
from tabulate import tabulate
import matplotlib.pyplot as plt

# Importar el diseño generado por Qt Designer
from MENU_PRINCIPAL import Ui_MainWindow as MenuPrincipalWindow  # Diseño del menú principal
from ventana_resultados import Ui_MainWindow as ResultadosWindow  # Diseño de la segunda ventana


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear el stacked widget para cambiar entre vistas
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Inicializar la vista del menú principal con el diseño generado
        self.menu_widget = QMainWindow()
        self.vista_menu = MenuPrincipalWindow()
        self.vista_menu.setupUi(self.menu_widget)

        # Agregar el menú principal al stacked_widget
        self.stacked_widget.addWidget(self.menu_widget)

        # Crear la segunda vista (resultados) con el diseño generado
        self.resultados_widget = QMainWindow()
        self.vista_resultados = ResultadosWindow()
        self.vista_resultados.setupUi(self.resultados_widget)

        # Asegurarse de que el scroll area ocupe todo el espacio
        self.vista_resultados.scrollArea.setWidgetResizable(True)

        # Crear un contenedor para el contenido del scroll
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.vista_resultados.scrollArea.setWidget(self.scroll_content)

        # Agregar la vista de resultados al stacked_widget
        self.stacked_widget.addWidget(self.resultados_widget)

        # Conectar el botón "Iniciar Reducción" a la lógica
        self.vista_menu.pushButton_2.clicked.connect(self.iniciar_reduccion)

        # Conectar el botón "Volver al menú principal" de la ventana de resultados
        self.vista_resultados.boton_volver_menu.clicked.connect(self.volver_menu_principal)

    def iniciar_reduccion(self):
        # Limpiar el contenido del área de scroll antes de añadir nuevos resultados
        while self.scroll_layout.count():
            child = self.scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Obtener los minterms ingresados por el usuario desde la línea de entrada
        minterms_text = self.vista_menu.lineEdit.text()

        try:
            # Convertir los minterms ingresados por el usuario
            self.minterms = sorted(list(map(int, minterms_text.split(','))))
            self.reduccion = Reduccion(self.minterms)

            # Generar la tabla de verdad
            tabla_verdad, num_bits = self.reduccion.crear_tabla_verdad()
            headers = list(string.ascii_uppercase[:num_bits]) + ['Salida']
            tabla_formateada = tabulate(tabla_verdad, headers=headers, tablefmt="grid")
            #tabla_formateada = "\n".join(["\t".join(map(str, fila)) for fila in tabla_verdad])

            # Mostrar la tabla de verdad en el área de texto
            tabla_verdad_output = QTextEdit(self.scroll_content)
            tabla_verdad_output.setReadOnly(True)
            tabla_verdad_output.setText(f"{tabla_formateada}")
            self.scroll_layout.addWidget(tabla_verdad_output)

            # Inicializar (Mostrar toda la informacion referente al MUX)
            informacion_output = QTextEdit(self.scroll_content) # Aquí se imprime la informacion
            informacion_output.setReadOnly(True)

            # el número de entradas iniciales
            numero_variables = self.reduccion.calcular_variables(self.minterms)
            impresion_numero_entradas=self.mostrar_num_entradas(numero_variables) #####

            

            # Mostrar las variables selectoras
            numero_variables_selectoras,variable_control = self.reduccion.asignar_variable_control(numero_variables)
            impresion_variables_selectoras=self.mostrar_variables_selectoras(numero_variables, numero_variables_selectoras) #####

            # Mostrar variable de control a utilizar
            impresion_variable_de_control=self.mostrar_variable_control(variable_control) ######

            # Mostrar el número de entradas reducidas
            numero_entradas = self.reduccion.recalcular_entradas(numero_variables_selectoras)
            impresion_variables_reducidas=self.mostrar_num_variables_reducidas(numero_entradas)######

            # Generar tabla final
            tabla,columnas=self.reduccion.generar_tabla_mux(numero_variables)
            impresion_tabla_final=self.imprimir_tabla_final(tabla,columnas)

            # Generar tabla MUX
            tabla_marcada,columnas_tabla_marcada,fila_A_negada_marcada, fila_A_marcada=self.reduccion.generar_tabla_mux_binarios(numero_variables)
            impresion_tabla_mux_final=self.imprimir_tabla_final(tabla_marcada,columnas_tabla_marcada)


            # AGREGAR TODA LA INFORMACION DE LA REDUCCION EN LA VENTANA
            informacion_output.setText(f"{impresion_numero_entradas}{impresion_variables_selectoras}\n{impresion_variable_de_control}\n{impresion_variables_reducidas}\n\n{impresion_tabla_final}\n\n{impresion_tabla_mux_final}")
            self.scroll_layout.addWidget(informacion_output)

            # IMPRIMIR EL RESULTADO FINAL DE LA REDUCCIÓN
            resultado = self.reduccion.comparar_columnas(fila_A_negada_marcada, fila_A_marcada)
            self.imprimir_resultado(resultado)


            # Llama a la función para dibujar el MUX, pasando los resultados
            self.dibujar_mux(numero_entradas, resultado)



            # Cambiar a la vista de resultados
            self.stacked_widget.setCurrentWidget(self.resultados_widget)

        except ValueError:
            error_output = QLabel("Error: Entrada inválida. Ingrese números separados por comas.")
            self.scroll_layout.addWidget(error_output)
            self.stacked_widget.setCurrentWidget(self.resultados_widget)


    def mostrar_num_entradas(self, numero_variables):
        #resultados_output= QTextEdit(self.scroll_content)
        #resultados_output.setReadOnly(True)
        numero_entradas = 2 ** numero_variables
        impresion=(f"Numero de entradas del MUX: {numero_entradas}\n")
        return impresion
        #self.scroll_layout.addWidget(resultados_output)
        #label_entradas = QLabel(f"Numero de entradas iniciales del MUX: {numero_entradas}")
        #self.scroll_layout.addWidget(label_entradas)



    def mostrar_variables_selectoras(self, numero_variables_iniciales, numero_variables_selectoras):
        impresion=(f"Número de variables selectoras iniciales: {numero_variables_iniciales}\nNúmero de variables selectoras después de la reducción: {numero_variables_selectoras}")
        return impresion
        #label_selectoras_iniciales = QLabel(f"Número de variables selectoras iniciales: {numero_variables_iniciales}")
        #self.scroll_layout.addWidget(label_selectoras_iniciales)


    def mostrar_variable_control(self,variable_control):
        impresion=(f"Variable de control: {variable_control}")
        return impresion

    def mostrar_num_variables_reducidas(self, numero_entradas):
        impresion=(f"Número de entradas del MUX luego de la reducción: {numero_entradas}")
        return impresion
        #label_entradas_reducidas = QLabel(f"Número de entradas del MUX luego de la reducción: {numero_entradas}")
        #self.scroll_layout.addWidget(label_entradas_reducidas)

    def imprimir_tabla_final(self, tabla, columnas):
        # Formatear todos los números en la tabla para que tengan dos dígitos
        tabla_formateada = [[f"{elemento:02d}" if isinstance(elemento, int) else str(elemento) for elemento in fila] for fila in tabla]
        # Crear una tabla formateada con tabulate
        tabla_final = tabulate(tabla_formateada, headers=[""] + columnas, tablefmt="grid")
        #tabla_formateada = tabulate(tabla, headers=[""] + columnas, tablefmt="grid")
        return tabla_final
    
    def imprimir_resultado(self,resultado):
        resultados_output=QLabel(f"RESULTADO FINAL: {resultado}")
        self.scroll_layout.addWidget(resultados_output)

    def volver_menu_principal(self):
        # Limpiar resultados para la siguiente ejecución
        while self.scroll_layout.count():
            child = self.scroll_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Cambiar de nuevo a la vista del menú principal
        self.stacked_widget.setCurrentWidget(self.menu_widget)

    def dibujar_mux(self,numero_entradas, resultados):
        fig, ax = plt.subplots(figsize=(8, 6))  # Aumentar el tamaño de la figura para más espacio

        # Dibujar entradas
        for i in range(numero_entradas):
            ax.plot([0, 1], [numero_entradas - i, numero_entradas - i], 'k-', lw=2)
            # Mostrar la entrada con su resultado
            ax.text(-0.1, numero_entradas - i, f'Entrada {i}: {resultados[i]}', 
                    verticalalignment='center', horizontalalignment='right')

        # Dibujar salida
        ax.plot([2, 3], [numero_entradas / 2, numero_entradas / 2], 'k-', lw=2)
        ax.text(3.1, numero_entradas / 2, 'Salida', 
                verticalalignment='center', horizontalalignment='left')

        # Dibujar línea de control (selector)
        ax.plot([1, 1], [0, numero_entradas], 'k--', lw=2)  # Línea de selección
        ax.text(1.5, numero_entradas / 2, f'MUX {numero_entradas} x 1',
                verticalalignment='center', horizontalalignment='center', 
                fontsize=12, fontweight='bold')

        # Ajustar los límites del gráfico para que se vea mejor
        ax.set_xlim(-0.5, 3.5)  # Ajuste horizontalmente
        ax.set_ylim(0, numero_entradas + 1)  # Ajuste verticalmente según el número de entradas

        # Quitar los ejes
        ax.axis('off')
        
        plt.title('Representación del MUX')
        plt.show()


if __name__ == "__main__":
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec_()









