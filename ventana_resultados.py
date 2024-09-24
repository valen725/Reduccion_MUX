from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1123, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1123, 700))
        MainWindow.setStyleSheet("background-image: url(:/cct/fondo.jpg);\n"
"")

        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout principal para todo el contenido (botones, etiquetas, scroll)
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Botón para volver al menú principal
        self.boton_volver_menu = QtWidgets.QPushButton(self.centralwidget)
        self.boton_volver_menu.setStyleSheet("font: 700 10pt 'Times New Roman'; background-color: white;")
        self.boton_volver_menu.setObjectName("boton_volver_menu")
        self.main_layout.addWidget(self.boton_volver_menu)  # Añadir botón al layout principal

        # Etiqueta de resultados
        self.label_resultados = QtWidgets.QLabel(self.centralwidget)
        self.label_resultados.setStyleSheet("font: 50pt 'Segoe UI'; color: rgb(85, 255, 255);")
        self.label_resultados.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.label_resultados)  # Añadir etiqueta al layout principal

        # ScrollArea que ocupará todo el espacio restante
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.main_layout.addWidget(self.scrollArea)  # Añadir scroll area al layout principal

        # Widget interno del scroll area (donde irá el contenido dinámico)
        self.scrollContents = QtWidgets.QWidget()
        self.scrollContents.setGeometry(QtCore.QRect(0, 0, 1101, 581))
        self.scrollArea.setWidget(self.scrollContents)

        # Layout dentro del scroll area para los resultados dinámicos
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scrollContents)

        # Ajustar el layout principal como el layout de centralwidget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menubar y statusbar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("ReduccionMUX", "ReduccionMUX"))
        self.boton_volver_menu.setText(_translate("MainWindow", "VOLVER AL MENU PRINCIPAL"))
        self.label_resultados.setText(_translate("MainWindow", "RESULTADOS"))
