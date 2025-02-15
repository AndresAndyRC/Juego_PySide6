from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
# Importamos los estilos desde un archivo externo
from styles import estilos_menu

class Menu(QMainWindow):
    def setupUi(self):
        """
        Configura la interfaz de usuario del menú principal.
        """
        self.setWindowTitle("Menu")  # Establece el título de la ventana
        self.resize(450, 500)  # Define el tamaño de la ventana

        # Creamos un layout principal de tipo vertical
        self.layout = QVBoxLayout()

        # Creamos un frame para el título
        self.frame_titulo = QFrame()
        
        # Creamos un frame para los inputs
        self.frame_input = QFrame()
       
        # Agregamos los frames al layout con proporciones definidas
        self.layout.addWidget(self.frame_titulo, 30)  # 30% del espacio para el título
        self.layout.addWidget(self.frame_input, 70)  # 70% del espacio para los inputs

        # Creamos un widget contenedor y le asignamos el layout
        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        # Establecemos el widget como el contenido central de la ventana
        self.setCentralWidget(self.widget)
        
        # Aplicamos el estilo definido en estilos_menu
        self.setStyleSheet(estilos_menu)

        # Llamamos los métodos para configurar los elementos internos
        self.setup_title()
        self.setup_inputs()

    def setup_title(self):
        """
        Configura el frame que contiene el título del menú.
        """
        # Creamos una etiqueta para el título
        self.titulo1 = QLabel("Bienvenido al juego", objectName="titulo1", alignment=Qt.AlignCenter)
        
        # Creamos un layout vertical para organizar el título
        self.layout_titulo = QVBoxLayout()
        self.layout_titulo.addWidget(self.titulo1)  # Agregamos el título al layout
        
        # Asignamos el layout al frame del título
        self.frame_titulo.setLayout(self.layout_titulo)

    def setup_inputs(self):
        """
        Configura el frame que contiene los inputs y el botón de inicio.
        """
        # Creamos una etiqueta con la instrucción para ingresar los nombres
        self.titulo2 = QLabel("Ingrese los nombres de los jugadores", alignment=Qt.AlignCenter)

        # Creamos los campos de entrada para los nombres de los jugadores
        self.player1 = QLineEdit(placeholderText="Jugador 1")
        self.player2 = QLineEdit(placeholderText="Jugador 2")

        # Creamos el botón para iniciar el juego
        self.btn_jugar = QPushButton("Jugar")
        
        # Creamos un layout vertical para organizar los elementos
        self.layout_input = QVBoxLayout()

        # Lista de widgets a agregar al layout
        widgets = [self.titulo2, self.player1, self.player2, self.btn_jugar]
        
        # Agregamos cada widget al layout con un espacio entre ellos
        for w in widgets:
            self.layout_input.addWidget(w)
            self.layout_input.addSpacing(10)  # Espacio de 10px entre elementos

        # Agregamos un estiramiento al final para distribuir mejor el espacio
        self.layout_input.addStretch()

        # Asignamos el layout al frame de inputs
        self.frame_input.setLayout(self.layout_input)


