import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class LoginWindow(QWidget):
    def __init__(window):
        super().__init__()
        window.setWindowTitle("Login")
        window.resize(250,300)

        layout = QVBoxLayout()

        window.username_label = QLabel("Username:")
        window.username_input = QLineEdit()
        layout.addWidget(window.username_label, alignment=Qt.AlignCenter)
        layout.addWidget(window.username_input)

        window.password_label = QLabel("Password:")
        window.password_input = QLineEdit()
        window.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(window.password_label, alignment=Qt.AlignCenter)
        layout.addWidget(window.password_input)

        window.login_button = QPushButton("Login")
        window.login_button.clicked.connect(window.login)
        layout.addWidget(window.login_button)

        window.error_label = QLabel()
        layout.addWidget(window.error_label, alignment=Qt.AlignCenter)

        window.setLayout(layout)

    def login(window):
        username = window.username_input.text()
        password = window.password_input.text()
        if username == "user" and password == "pass":
            window.error_label.setText("Login successful!")
            window.hide()
            ofice.show()
        else:
            window.error_label.setText("Invalid username or password")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    ofice = QWidget()
    ofice.resize(600, 500)
    ofice.setWindowTitle('Ofice')
    ofice.hide()
    window.show()
    sys.exit(app.exec_())