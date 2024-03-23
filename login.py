# Импорты
import sys
from base import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

# Клас для окна для логина
class studentWindow(QWidget):
    def __init__(window):
        super().__init__()
        window.setWindowTitle("Login")
        window.resize(250, 300)
        window.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        window.username_label = QLabel("Username:")
        window.username_input = QLineEdit()
        
        layout.addWidget(window.username_input)

        window.password_label = QLabel("Password:")
        window.password_input = QLineEdit()
        window.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(window.password_label)
        layout.addWidget(window.password_input)

        window.login_button = QPushButton("Login")
        window.login_button.clicked.connect(window.login)
        layout.addWidget(window.login_button)

        window.error_label = QLabel()
        layout.addWidget(window.error_label)

        window.setLayout(layout)

    def login(window):
        login_input = window.username_input.text()
        pas_input = window.password_input.text()
        data = get_data(login_input)
        if pas_input == data[0][4]:
            print(data)
            window.hide()
            ofice.show()
        else:
            window.error_label.setText("Invalid username or password")
# Клас для окна для офиса
class studenOficetWindow(QWidget):
    def __init__(ofice):
        super().__init__()
        # Название для окна логина
        ofice.setWindowTitle("Student account")
        # Размеры логин окна
        ofice.resize(310,300)
        # Основная вертикальная линия
        layout_for_ofice = QVBoxLayout()
        # Info
        ofice.info_name = QLabel()
        layout_for_ofice.addWidget(ofice.info_name)
        ofice.info_class = QLabel()
        layout_for_ofice.addWidget(ofice.info_class)
        ofice.info_avr_score = QLabel()
        layout_for_ofice.addWidget(ofice.info_avr_score)
        # Основная вертикальная линия прикрипляеться к окну
        ofice.setLayout(layout_for_ofice)

# Основные событие
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = studentWindow()
    ofice = studenOficetWindow()
    ofice.hide()
    window.show()
    sys.exit(app.exec_())