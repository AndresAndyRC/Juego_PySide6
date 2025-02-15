from PySide6.QtWidgets import *
from menu import Menu
from game import Game
import sys

class Triqui:
    def __init__(self):
        self.menu = Menu()
        self.game = Game()

        self.menu.setupUi()
        self.game.setupUi()

        self.menu.btn_jugar.clicked.connect(self.abrir_juego)

    def abrir_juego(self):
        self.menu.hide()
        self.game.show()  

        self.game.titulo(self.menu.player1.text(), self.menu.player2.text()) 

app = QApplication(sys.argv)      

main = Triqui()
main.menu.show()

sys.exit(app.exec())