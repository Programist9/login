# Импорты
import time
import sys
from base import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

# Клас для окна для логина
class studentWindow(QWidget):
    def __init__(window):
        super().__init__()
        window.setWindowTitle("Log in")
        window.setFixedSize(260, 300)
        window.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        window.username_label = QLabel("Username:")
        window.username_input = QLineEdit()
        
        layout.addWidget(window.username_label)
        layout.addWidget(window.username_input)

        window.password_label = QLabel("Password:")
        window.password_input = QLineEdit()
        window.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(window.password_label)
        layout.addWidget(window.password_input)

        window.login_button = QPushButton("Log in")
        window.login_button.clicked.connect(window.login)
        layout.addWidget(window.login_button)

        window.back_button = QPushButton("Back")
        window.back_button.clicked.connect(window.back)
        layout.addWidget(window.back_button)

        window.error_label = QLabel()
        layout.addWidget(window.error_label)

        window.setLayout(layout)
    def back(window):
        window.hide()
        menu.show()
    def login(window):
        login_input = window.username_input.text()
        pas_input = window.password_input.text()
        data = get_data(login_input)
        if data:
            if pas_input == data[0][4]:
                window.error_label.setText("")
                print(data)
                window.hide()
                ofice.show()
                ofice.info_name.setText("Имя ученика: " + data[0][1])
                ofice.info_class.setText("Класс ученика: " + data[0][2])
                ofice.info_avr_score.setText("Средний балл ученика: " + str(data[0][3]))
            else:
                window.error_label.setText("Invalid password")
                QTimer.singleShot(4000, lambda: window.error_label.setText(""))
        else:
            window.error_label.setText("Empty or invalid username")
            QTimer.singleShot(4000, lambda: window.error_label.setText(""))
# Клас для окна для офиса
class studenOficetWindow(QWidget):
    def __init__(ofice):
        super().__init__()
        # Название для окна логина
        ofice.setWindowTitle("Student account")
        # Размеры логин окна
        ofice.setFixedSize(330,300)
        window.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        # Основная вертикальная линия
        layout_for_ofice = QVBoxLayout()
        # Info

        ofice.info_name = QLabel()
        layout_for_ofice.addWidget(ofice.info_name)

        ofice.info_class = QLabel()
        layout_for_ofice.addWidget(ofice.info_class)

        ofice.info_avr_score = QLabel()
        layout_for_ofice.addWidget(ofice.info_avr_score)

        ofice.log_out_button = QPushButton("Log out")
        ofice.log_out_button.clicked.connect(ofice.log_out)
        layout_for_ofice.addWidget(ofice.log_out_button)
        # Основная вертикальная линия прикрипляеться к окну
        ofice.setLayout(layout_for_ofice)
    def log_out(ofice):
        ofice.hide()
        window.show()

class mainMenu(QWidget):
    def __init__(menu):
        super().__init__()
        # Название для окна логина
        menu.setWindowTitle("Menu")
        # Размеры логин окна
        menu.setFixedSize(330,300)
        window.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        # Основная вертикальная линия
        layout_for_menu = QVBoxLayout()

        menu.log_in_button = QPushButton("Log in")
        menu.log_in_button.clicked.connect(menu.log_in)
        layout_for_menu.addWidget(menu.log_in_button)

        menu.sing_up_button = QPushButton("Sing up")
        menu.sing_up_button.clicked.connect(menu.sing_up)
        layout_for_menu.addWidget(menu.sing_up_button)
        # Основная вертикальная линия прикрипляеться к окну
        menu.setLayout(layout_for_menu)
    def log_in(menu):
        menu.hide()
        window.show()
    def sing_up(menu):
        menu.hide()
        sing_up.show()


class singUpWindow(QWidget):
    def __init__(windowforsingup):
        super().__init__()
        windowforsingup.setWindowTitle("Log in")
        windowforsingup.setFixedSize(260, 300)
        windowforsingup.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        windowforsingup.username_label = QLabel("Username:")
        windowforsingup.username_input = QLineEdit()
        
        layout.addWidget(windowforsingup.username_label)
        layout.addWidget(windowforsingup.username_input)

        windowforsingup.password_label = QLabel("Password:")
        windowforsingup.password_input = QLineEdit()
        windowforsingup.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(windowforsingup.password_label)
        layout.addWidget(windowforsingup.password_input)

        windowforsingup.singup_button = QPushButton("Sing up")
        windowforsingup.singup_button.clicked.connect(windowforsingup.singup)
        layout.addWidget(windowforsingup.singup_button)

        windowforsingup.back_button = QPushButton("Back")
        windowforsingup.back_button.clicked.connect(windowforsingup.back)
        layout.addWidget(windowforsingup.back_button)

        windowforsingup.error_label = QLabel()
        layout.addWidget(windowforsingup.error_label)

        windowforsingup.setLayout(layout)
    def back(windowforsingup):
        windowforsingup.hide()
        menu.show()
    def singup(windowforsingup):
        print('singed up')
        windowforsingup.hide()
        window.show()
# Основные событие
app = QApplication(sys.argv)
window = studentWindow()
ofice = studenOficetWindow()
menu = mainMenu()
sing_up = singUpWindow()
menu.show()
sys.exit(app.exec_())