# Импорты
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
# Клас для окна для логина
class LoginWindow(QWidget):
    def __init__(window):
        super().__init__()
        # Название для окна логина
        window.setWindowTitle("Login")
        # Размеры логин окна
        window.resize(250,300)
        # Основная вертикальная линия
        layout = QVBoxLayout()
        # Юзернэйм текст создаётся
        window.username_label = QLabel("Username:")
        window.username_input = QLineEdit()
        # Юзернэйм текст прикрипляется
        layout.addWidget(window.username_label, alignment=Qt.AlignCenter)
        layout.addWidget(window.username_input)
        # Пароль текст создаётся
        window.password_label = QLabel("Password:")
        window.password_input = QLineEdit()
        # Логика кнопки
        window.password_input.setEchoMode(QLineEdit.Password)
        # Пароль текст прикрипляется
        layout.addWidget(window.password_label, alignment=Qt.AlignCenter)
        layout.addWidget(window.password_input)
        # Кнопка логин создаётся
        window.login_button = QPushButton("Login")
        # Кнопка логин прикрипляеться
        window.login_button.clicked.connect(window.login)
        layout.addWidget(window.login_button)
        # Error alert/уведомление
        window.error_label = QLabel()
        layout.addWidget(window.error_label, alignment=Qt.AlignCenter)
        # Основная вертикальная линия прикрипляеться к окну
        window.setLayout(layout)
    # Логика пароля
    def login(window):
        username = window.username_input.text()
        password = window.password_input.text()
        if username == "user" and password == "pass":
            window.error_label.setText("Login successful!")
            window.hide()
            ofice.show()
        else:
            window.error_label.setText("Invalid username or password")

# Основные событие
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    ofice = QWidget()
    ofice.resize(600, 500)
    ofice.setWindowTitle('Ofice')
    ofice.hide()
    window.show()
    sys.exit(app.exec_())