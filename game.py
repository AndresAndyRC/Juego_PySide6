from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
# importamos los estilos
from styles import estilos_juego

class Game(QMainWindow):
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
        self.setStyleSheet(estilos_juego)

app = QApplication(sys.argv)
game = Game()
game.setupUi()
game.show()
sys.exit(app.exec())