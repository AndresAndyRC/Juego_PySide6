from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
# Importamos los estilos desde un archivo externo
from styles import estilos_juego

class Game(QMainWindow):
    """
    Clase que representa el juego de Tic-Tac-Toe.
    """
    
    # Variables de clase para gestionar el estado del juego
    current_player = "X"  # Jugador actual
    x_moves = set()  # Movimientos del jugador X
    o_moves = set()  # Movimientos del jugador O
    
    # Combinaciones ganadoras predefinidas
    winner_moves = [
        # Horizontales
        {"1,1", "1,2", "1,3"},
        {"2,1", "2,2", "2,3"},
        {"3,1", "3,2", "3,3"},
        # Verticales
        {"1,1", "2,1", "3,1"},
        {"1,2", "2,2", "3,2"},
        {"1,3", "2,3", "3,3"},
        # Diagonales
        {"1,1", "2,2", "3,3"},
        {"1,3", "2,2", "3,1"}
    ]

    def setupUi(self):
        """
        Configura la interfaz gráfica del juego.
        """
        self.setWindowTitle("Juego")
        self.resize(450, 500)

        # Crear los frames para el título y los botones del tablero
        self.frame_titulo = QFrame()
        self.frame_buttons = QFrame()

        # Crear el layout principal
        self.root_layout = QVBoxLayout()
        self.root_layout.addWidget(self.frame_titulo, 30)
        self.root_layout.addWidget(self.frame_buttons, 70)

        # Asignar el layout a un widget contenedor
        self.widget = QWidget()
        self.widget.setLayout(self.root_layout)
        self.setCentralWidget(self.widget)
        
        # Configurar los botones del tablero
        self.setup_buttons_frame()

        # Aplicar los estilos
        self.setStyleSheet(estilos_juego)

    def titulo(self, player1, player2):
        """
        Configura el título del juego con los nombres de los jugadores.
        :param player1: Nombre del primer jugador
        :param player2: Nombre del segundo jugador
        """
        self.titulo1 = QLabel(f"{player1}  VS {player2}", objectName="titulo1", alignment=Qt.AlignCenter)
        
        # Crear layout y asignarlo al frame
        self.layout_titulo = QVBoxLayout()
        self.layout_titulo.addWidget(self.titulo1)
        self.frame_titulo.setLayout(self.layout_titulo)

    def add_button_to_layout(self, row, column):
        """
        Crea y añade un botón en la posición especificada en el tablero.
        :param row: Fila del botón
        :param column: Columna del botón
        """
        coordinates = f'{row},{column}'
        button = QPushButton()
        button.clicked.connect(lambda: self.record_move(coordinates, button))
        self.buttons_layout.addWidget(button, row, column)

    def setup_buttons_frame(self):
        """
        Configura la cuadrícula de botones del juego (tablero 3x3).
        """
        self.buttons_layout = QGridLayout()

        # Crear los botones de forma dinámica y añadirlos al layout
        for row in range(1, 4):
            for column in range(1, 4):
                self.add_button_to_layout(row, column)

        self.frame_buttons.setLayout(self.buttons_layout)

    def record_move(self, coordinates, button):
        """
        Registra el movimiento del jugador y actualiza el botón seleccionado.
        :param coordinates: Coordenadas del botón en formato "fila,columna"
        :param button: Objeto QPushButton que fue presionado
        """
        button.setText(self.current_player)
        button.setEnabled(False)
        
        # Guardar el movimiento del jugador actual
        if self.current_player == "X":
            self.x_moves.add(coordinates)
            self.verify_moves()
            self.current_player = "O"
        else: 
            self.o_moves.add(coordinates)
            self.verify_moves()
            self.current_player = "X"    

    def verify_moves(self):
        """
        Verifica si hay un ganador tras cada movimiento.
        """
        player_moves = self.x_moves if self.current_player == "X" else self.o_moves

        for move in self.winner_moves:
            if move.issubset(player_moves):
                print(self.current_player, "Ganaste!!")
