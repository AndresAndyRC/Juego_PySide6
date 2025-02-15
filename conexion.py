from PySide6.QtWidgets import *
from menu import Menu
from game import Game
import sys

class Triqui:
    """
    Clase principal del juego que gestiona la interacción entre el menú y el juego.
    """
    def __init__(self):
        """
        Inicializa la aplicación, creando las instancias del menú y el juego.
        """
        self.menu = Menu()  # Instancia de la ventana del menú principal
        self.game = Game()  # Instancia de la ventana del juego

        # Configurar las interfaces gráficas
        self.menu.setupUi()
        self.game.setupUi()

        # Conectar el botón de jugar del menú con la función abrir_juego
        self.menu.btn_jugar.clicked.connect(self.abrir_juego)

    def abrir_juego(self):
        """
        Oculta el menú y muestra la ventana del juego con los nombres ingresados por los jugadores.
        """
        self.menu.hide()  # Oculta la ventana del menú
        self.game.show()  # Muestra la ventana del juego

        # Configura el título del juego con los nombres ingresados por los jugadores
        self.game.titulo(self.menu.player1.text(), self.menu.player2.text())

# Crear la aplicación Qt
app = QApplication(sys.argv)      

# Instanciar y mostrar el menú principal
main = Triqui()
main.menu.show()

# Ejecutar el loop de eventos de la aplicación
sys.exit(app.exec())
