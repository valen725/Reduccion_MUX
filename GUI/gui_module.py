# gui/gui_module.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt
from reduccion.reduccion_module import Reduccion  # Importamos la lógica de reducción
import string

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuramos la ventana principal
        self.setWindowTitle('Reducción MUX')
        self.setGeometry(100, 100, 800, 600)

        # Agregar una imagen de fondo (opcional)
        self.label_fondo = QLabel(self)
        self.pixmap = QPixmap("fondo.png")  # Asegúrate de tener la imagen en tu directorio
        self.label_fondo.setPixmap(self.pixmap)
        self.label_fondo.setGeometry(0, 0, 800, 600)

        # Campo para ingresar los minterms
        self.label_minterms = QLabel("Ingrese los minterms:", self)
        self.label_minterms.setGeometry(50, 50, 200, 30)
        self.entry_minterms = QLineEdit(self)
        self.entry_minterms.setGeometry(200, 50, 400, 30)

        # Botón para generar la tabla de verdad
        self.btn_generar = QPushButton('Generar Tabla de Verdad', self)
        self.btn_generar.setGeometry(300, 100, 200, 40)
        self.btn_generar.clicked.connect(self.generar_tabla_verdad)

    def generar_tabla_verdad(self):
        minterms_text = self.entry_minterms.text()

        try:
            # Convertir los minterms ingresados por el usuario
            minterms = sorted(list(map(int, minterms_text.split(','))))

            # Usar el módulo de Reduccion para generar la tabla de verdad
            reduccion = Reduccion(minterms)
            tabla_verdad, num_bits = reduccion.crear_tabla_verdad()

            # Mostramos la tabla de verdad en una ventana emergente
            headers = list(string.ascii_uppercase[:num_bits]) + ['Salida']
            tabla_formateada = "\n".join(["\t".join(map(str, fila)) for fila in tabla_verdad])
            QMessageBox.information(self, "Tabla de Verdad", f"{headers}\n{tabla_formateada}")

            # Mostrar el número de entradas iniciales
            numero_variables = reduccion.calcular_variables(minterms)
            self.mostrar_num_entradas(numero_variables)

            # Asignar variables selectoras
            numero_variables_selectoras = reduccion.asignar_variable_control(numero_variables)
            self.mostrar_variables_selectoras(numero_variables, numero_variables_selectoras)

            # Recalcular entradas y mostrar
            numero_entradas = reduccion.recalcular_entradas(numero_variables_selectoras)
            self.mostrar_num_variables_reducidas(numero_entradas)

        except ValueError:
            # Mostrar error si la entrada no es válida
            QMessageBox.critical(self, "Error", "Entrada inválida. Ingrese números separados por comas.")

    def mostrar_num_entradas(self, numero_variables):
        numero_entradas = 2 ** numero_variables
        QMessageBox.information(self, "Número de Entradas", f"Número de entradas iniciales del MUX: {numero_entradas}")

    def mostrar_variables_selectoras(self, numero_variables_iniciales, numero_variables_selectoras):
        QMessageBox.information(self, "Variables Selector", 
                            f"Número de variables selectoras iniciales: {numero_variables_iniciales}\n"
                            f"Número de variables selectoras después de la reducción: {numero_variables_selectoras}")

    def mostrar_num_variables_reducidas(self, numero_entradas):
        QMessageBox.information(self, "Variables Reducidas", f"Número de entradas del MUX luego de la reducción: {numero_entradas}")



