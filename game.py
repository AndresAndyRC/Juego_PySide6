from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
# importamos los estilos
from styles import estilos_juego

class Game(QMainWindow):
    current_player = "X"
    x_moves = set()
    o_moves = set()
    winner_moves = [
        # Horizontal
        {"1,1", "1,2", "1,3"},
        {"2,1", "2,2", "2,3"},
        {"3,1", "3,2", "3,3"},
        # Vertical
        {"1,1", "2,1", "3,1"},
        {"1,2", "2,2", "3,2"},
        {"1,3", "2,3", "3,3"},
        # Diagonal
        {"1,1", "2,2", "3,3"},
        {"1,3", "2,2", "3,1"}
    ]

    def setupUi(self):
        self.setWindowTitle("Juego")
        self.resize(450, 500)

        self.frame_titulo = QFrame()
        self.frame_buttons = QFrame()

        self.root_layout = QVBoxLayout()
        self.root_layout.addWidget(self.frame_titulo, 30)
        self.root_layout.addWidget(self.frame_buttons, 70)

        self.widget = QWidget()
        self.widget.setLayout(self.root_layout)

        self.setCentralWidget(self.widget)
        self.setup_buttons_frame()

        self.setStyleSheet(estilos_juego)

    def add_button_to_layout(self, row, column):
        
        coordinates = f'{row},{column}'
        button = QPushButton(coordinates)
        button.clicked.connect(lambda: self.record_move(coordinates, button))
        self.buttons_layout.addWidget(button, row, column)

    def setup_buttons_frame(self):
        """
            El for hace lo mismo que las lineas comentadas, crea los botones y pos posiciona en el layout
        """
        # self.button1 = QPushButton()
        # self.button2 = QPushButton()
        # self.button3 = QPushButton()
        # self.button4 = QPushButton()
        # self.button5 = QPushButton()
        # self.button6 = QPushButton()
        # self.button7 = QPushButton()
        # self.button8 = QPushButton()
        # self.button9 = QPushButton()    

        self.buttons_layout = QGridLayout()

        # self.buttons_layout.addWidget(self.button1, 0, 0)
        # self.buttons_layout.addWidget(self.button2, 0, 1)
        # self.buttons_layout.addWidget(self.button3, 0, 2)
        # self.buttons_layout.addWidget(self.button4, 1, 0)
        # self.buttons_layout.addWidget(self.button5, 1, 1)
        # self.buttons_layout.addWidget(self.button6, 1, 2)
        # self.buttons_layout.addWidget(self.button7, 2, 0)
        # self.buttons_layout.addWidget(self.button8, 2, 1)
        # self.buttons_layout.addWidget(self.button9, 2, 2)

        for row in range(1, 4):
            for column in range(1, 4):
                self.add_button_to_layout(row, column)

        self.frame_buttons.setLayout(self.buttons_layout)

    def record_move(self, coordinates, button):
        button.setText(self.current_player)
        button.setEnabled(False)
        if (self.current_player == "X"):
            self.x_moves.add(coordinates)
            self.verify_moves()
            self.current_player = "O"
        else: 
            self.o_moves.add(coordinates)
            self.verify_moves()
            self.current_player = "X"    
        print(coordinates) 

    def verify_moves(self):
        if (self.current_player == "X"):
            player_moves = self.x_moves
        else:
            player_moves = self.o_moves

        for move in self.winner_moves:
            if (move.issubset(player_moves)):
                print(self.current_player, "Ganaste!!")


app = QApplication(sys.argv)
game = Game()
game.setupUi()
game.show()
sys.exit(app.exec())