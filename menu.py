from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
# importamos los estilos
from styles import estilos_menu

class Menu(QMainWindow):
    def setupUi(self):
        self.setWindowTitle("Menu")
        self.resize(450, 500)

        # creamos un layaout ( un layaout es un contenedor de widgets que pasa los padres a los widgets hijos)

        self.layout = QVBoxLayout()

        # creamos una frame 
        self.frame_titulo = QFrame()
        
        # creamos un input
        self.frame_input = QFrame()
       
        # agregamos los frame al layout
        self.layout.addWidget(self.frame_titulo, 30) # el 30 es el porcentaje de espacio que ocupara el frame
        self.layout.addWidget(self.frame_input, 70)

        # creammos el QWidget
        self.widget = QWidget()
        # agregamos el layout al widget
        self.widget.setLayout(self.layout)

        # agregamos el widget al QMainWindow
        self.setCentralWidget(self.widget)
        # le damos estilo al QMainWindow
        self.setStyleSheet(estilos_menu)

        # llamamos el metodo para agregar un titulo al frame
        self.setup_title()
        self.setup_inputs()

    # creamos un metodo para agregar un titulo al frame
    def setup_title(self):
        # creamos un titulo
        self.titulo1 = QLabel("Bienvenido al juego", objectName="titulo1", alignment=Qt.AlignCenter)
        # creamos un layout para el titulo
        self.layout_titulo = QVBoxLayout()
        # agregamos el titulo al layout
        self.layout_titulo.addWidget(self.titulo1)
        # agregamos el frame que contiene el titulo
        self.frame_titulo.setLayout(self.layout_titulo)

    # creamos un metodo para agregar los inputs al frame
    def setup_inputs(self):

        # creamos un titulo
        self.titulo2 = QLabel("Ingrese los nombres de los jugadores", alignment=Qt.AlignCenter)

        # creamos los inputs

        self.player1 = QLineEdit(placeholderText="Jugador 1")
        self.player2 = QLineEdit(placeholderText="Jugador 2")

        # agregamos boton

        self.btn_jugar = QPushButton("Jugar")
        #self.btn_jugar.clicked.connect(self.jugar)
        # creamos un layout para los inputs

        self.layout_input = QVBoxLayout()

        # creamos un arreglo para abarcar los layouts de los inputs
        widgets = [self.titulo2, self.player1, self.player2, self.btn_jugar]
        # creamos un for que agrega los inputs al layout
        for w in widgets:
            self.layout_input.addWidget(w)
            #agregamos un espacio entre los inputs
            self.layout_input.addSpacing(10) # 10 es el tamaño del espacio en px

        # agregamos un espacio al final
        self.layout_input.addStretch()

        # agregamos el frame que contiene lo inputs

        self.frame_input.setLayout(self.layout_input)



app = QApplication(sys.argv)
menu = Menu()
menu.setupUi()
menu.show()
sys.exit(app.exec())