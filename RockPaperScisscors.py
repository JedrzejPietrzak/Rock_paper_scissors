import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from random import randint

font = QFont("Times", 18)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 250, 856, 450)
        self.setWindowTitle("Rock Paper Scissors Game")
        self.UI_1()
        self.show()
        
    
    def UI_1(self):
        self.widgets = []
        # Welcoming Labels
        self.welcome_label = QLabel("Welcome to the game!", self)
        self.welcome_label.move(250, 50)
        self.welcome_label.setFont(font)
        self.widgets.append(self.welcome_label)
        
        self.choose_style = QLabel("Do you want to play against the computer or the second player", self)
        self.choose_style.move(140, 90)
        self.choose_style.setFont(QFont("Times", 12))
        self.widgets.append(self.choose_style)
        
        # Radiobuttons for choosing number of players
        self.singleplayer = QRadioButton("singleplayer", self)
        self.singleplayer.move(180, 130)
        self.singleplayer.setStyleSheet("QRadioButton::indicator"
                                        "{"
                                        "width : 16 px;"
                                        "height : 16 px;"
                                        "}")
        self.singleplayer.setFont(QFont("Times", 12))
        self.singleplayer.clicked.connect(self.hide_inputs)
        self.widgets.append(self.singleplayer)
        
        self.multiplayer = QRadioButton("multiplayer", self)
        self.multiplayer.setStyleSheet("QRadioButton::indicator"
                                        "{"
                                        "width : 16 px;"
                                        "height : 16 px;"
                                        "}")
        self.multiplayer.move(180, 165)
        self.multiplayer.setFont(QFont("Times", 12))
        self.multiplayer.clicked.connect(self.provide_names_of_players)
        self.widgets.append(self.multiplayer)
        
        # Button to start the game!
        self.start_button = QPushButton('START!', self)
        self.start_button.move(350, 200)
        self.widgets.append(self.start_button)
        self.start_button.clicked.connect(self.clear_and_proceed)

    def provide_names_of_players(self):
        self.start_button.move(350, 250)
        self.name1 = QLineEdit(self)
        self.name1.setPlaceholderText("enter the name of the first player")
        self.name1.setGeometry(450, 160, 240, 20)
        self.name1.show()
        self.widgets.append(self.name1)
        
        self.name2 = QLineEdit(self)
        self.name2.setPlaceholderText("enter the name of the second player")
        self.name2.setGeometry(450, 190, 240, 20)
        self.name2.show()
        self.widgets.append(self.name2)
    
    def UI_singleplayer(self):
        lst = ['rock', 'paper', 'scissors']
        i = randint(0,2)
        self.p2_fig = lst[i]                # This here gets a random figure from the computer
        self.p1_name = 'Player'
        self.p2_name = "the computer"
        # Label to begin the second part of the game
        self.label = QLabel('Choose your figure', self)
        self.label.move(330, 50)
        self.label.setFont(QFont("Times", 14))
        self.label.show()
        
        # Buttons for r/p/s
        self.rock_btn = QPushButton(self)
        self.rock_btn.setGeometry(50, 150, 158, 161)
        self.rock_btn.setStyleSheet("background-image : url(Rock.jpg);")
        self.rock_btn.show()
        self.rock_btn.clicked.connect(self.rck_btn_func_splayer)
        
        self.scis_btn = QPushButton(self)
        self.scis_btn.setGeometry(350, 150, 156, 161)
        self.scis_btn.setStyleSheet("background-image : url(Scissors.jpg);")
        self.scis_btn.show()
        self.scis_btn.clicked.connect(self.scs_btn_func_splayer)
        
        self.pap_btn = QPushButton(self)
        self.pap_btn.setGeometry(650, 150, 156, 161)
        self.pap_btn.setStyleSheet("background-image : url(Paper.jpg);")
        self.pap_btn.show()
        self.pap_btn.clicked.connect(self.pap_btn_func_splayer)
        
        # Button to check with the computer!
        self.fight_btn = QPushButton("Fight!", self)
        self.fight_btn.setGeometry(390, 350, 80, 40)
        self.fight_btn.show()
        self.fight_btn.clicked.connect(self.fight_btn_func)
          
    def fight_btn_func(self):
        if self.p1_fig == self.p2_fig:
            self.outcome = 0
        elif self.p1_fig == 'rock' and self.p2_fig == 'scissors':
            self.outcome = 1 # 1 means p1 wins
        elif self.p1_fig == 'paper' and self.p2_fig == 'rock':
            self.outcome = 1
        elif self.p1_fig == 'scissors' and self.p2_fig == 'paper':
            self.outcome = 1
        else:
            self.outcome = -1
        if self.outcome == 0:
            text = 'draw'
        elif self.outcome == 1:
            text = f'{self.p1_name} wins!' 
        else:
            text = f'{self.p2_name} wins!'
        
        self.mbox = QMessageBox.information(self, 'Results!', text)
    
    def rck_btn_func_splayer(self):
        self.p1_fig = 'rock'
     
    def scs_btn_func_splayer(self):
        self.p1_fig = 'scissors'
            
    def pap_btn_func_splayer(self):
        self.p1_fig = 'paper'
            
    def UI_multiplayer(self):
        self.player_var = 1
        # Label to begin the second part of the game
        self.label = QLabel(f'{self.p1_name} Choose Your Figure', self)
        self.label.setGeometry(330, 50, 400, 50)
        self.label.setFont(QFont("Times", 14))
        self.label.show()
        
        # Buttons for r/p/s
        self.rock_btn = QPushButton(self)
        self.rock_btn.setGeometry(50, 150, 158, 161)
        self.rock_btn.setStyleSheet("background-image : url(Rock.jpg);")
        self.rock_btn.show()
        self.rock_btn.clicked.connect(self.rck_btn_func_mplayer)
        
        self.scis_btn = QPushButton(self)
        self.scis_btn.setGeometry(350, 150, 156, 161)
        self.scis_btn.setStyleSheet("background-image : url(Scissors.jpg);")
        self.scis_btn.show()
        self.scis_btn.clicked.connect(self.scs_btn_func_mplayer)
        
        self.pap_btn = QPushButton(self)
        self.pap_btn.setGeometry(650, 150, 156, 161)
        self.pap_btn.setStyleSheet("background-image : url(Paper.jpg);")
        self.pap_btn.show()
        self.pap_btn.clicked.connect(self.pap_btn_func_mplayer)
        
        # Button to check with the computer!
        self.fight_btn = QPushButton("Fight!", self)
        self.fight_btn.setGeometry(390, 350, 80, 40)
        self.fight_btn.show()
        self.fight_btn.clicked.connect(self.fight_btn_func)
   
    def rck_btn_func_mplayer(self):
        if self.player_var == 1:
            self.p1_fig = 'rock'
            self.label.setText(f'{self.p2_name} Choose Your Figure')
            self.player_var += 1
        else:
            self.p2_fig = 'rock'
        
   
    def scs_btn_func_mplayer(self):
        if self.player_var == 1:
            self.p1_fig = 'scissors'
            self.label.setText(f'{self.p2_name} Choose Your Figure')
            self.player_var += 1
        else:
            self.p2_fig = 'scissors'
    
    def pap_btn_func_mplayer(self):
        if self.player_var == 1:
            self.p1_fig = 'paper'
            self.label.setText(f'{self.p2_name} Choose Your Figure')
            self.player_var += 1
        else:
            self.p2_fig = 'paper'
        
   
        
    def hide_inputs(self):
        try:
            self.name1.deleteLater()
            self.name2.deleteLater()
        except AttributeError:
            pass
        except RuntimeError:
            pass
        
    def clear_and_proceed(self):
        try:
            self.p1_name = self.name1.text()
            self.p2_name = self.name2.text()
            for w in self.widgets:
                w.deleteLater()
        except AttributeError:
            pass
        except RuntimeError:
            pass
        if self.singleplayer.isChecked():
            self.UI_singleplayer()
        else:
            self.UI_multiplayer()
    
def main():      
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__ == "__main__":
    main()