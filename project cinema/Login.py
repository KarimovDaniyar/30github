from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox, QLabel
import sys
import Registration
import Movies
import requests


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()

        self.setWindowTitle("Log In")
        self.setGeometry(800, 250, 350, 450)
        self.setFixedSize(350,450)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c2c2c;
            }
        """)

        # Устанавливаем черный фон окна с помощью QPalette
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        # Создаем виджет для фона
        self.background_label = QLabel(self)
        self.background_label.setGeometry(self.rect())
        self.background_label.setPixmap(
            QtGui.QPixmap('.\images\macBack6.jpg').scaled(self.size(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
        self.background_label.setScaledContents(True)

        # Применяем эффект прозрачности
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.4)  # 50% прозрачности
        self.background_label.setGraphicsEffect(self.opacity_effect)

        self.login_text = QtWidgets.QLabel(self)
        self.login_text.setText("Login In Your Account")
        self.login_text.move(84, 20)
        self.login_text.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: 500;
                font-family: 'Arial Black', Gadget, sans-serif;
}

            }
        """)

        self.login_text.adjustSize()


        self.username = QtWidgets.QLineEdit(self)
        self.username.setFixedSize(200, 40)
        self.username.move(75, 60)
        self.username.setPlaceholderText("Username")
        self.username.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                border-radius: 6px;
                background-color: rgba(255, 255, 255, 0.4);  /* Белый фон с прозрачностью */
                color: black;  /* Цвет текста */
                padding-left: 8px;
                border: 2px solid #211E1E;  /* Обводка */
            }
        """)

        self.password = QtWidgets.QLineEdit(self)
        self.password.setFixedSize(200, 40)
        self.password.move(75, 130)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                border-radius: 6px;
                background-color: rgba(255, 255, 255, 0.4);  /* Белый фон с прозрачностью */
                color: black;  /* Цвет текста */
                padding-left: 8px;
                border: 2px solid #211E1E;  /* Обводка */
            }
        """)

        self.robot_box = QtWidgets.QCheckBox(self)
        self.robot_box.setText("I'm not a robot")
        self.robot_box.move(119, 200)
        self.robot_box.setStyleSheet("""
            QCheckBox {
                color: white;
                font-size: 15px;
            }
        """)
        self.robot_box.adjustSize()

        self.question_text = QtWidgets.QLabel(self)
        self.question_text.setText("Don't Have Account ?")
        self.question_text.move(116, 320)
        self.question_text.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;
            }
        """)
        self.question_text.adjustSize()


        self.login_btn = QtWidgets.QPushButton(self)
        self.login_btn.move(112, 260)
        self.login_btn.setText("Log In")
        self.login_btn.setFixedSize(125, 40)
        self.login_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                border: 2px solid #211E1E;
                font-size: 17px;
                
            }
            QPushButton:hover {
                background-color: #544CAE;
                border: 2px solid #211E1E;
            }
            
        """)
        self.login_btn.clicked.connect(self.login)

        self.signup_btn = QtWidgets.QPushButton(self)
        self.signup_btn.move(112, 350)
        self.signup_btn.setText("Sign Up")
        self.signup_btn.setFixedSize(125, 40)
        self.signup_btn.setStyleSheet("""
            QPushButton {
                background-color: #211E1E;
                color: white;
                
                border-radius: 10px;
                border: 2px solid #3e8e41;
                font-size: 17px;
            }
            QPushButton:hover {
                background-color: #544CAE;
                border: 2px solid #211E1E;
            }
        """)
        self.signup_btn.clicked.connect(self.open_registration)

    def get_history(self):
        response = requests.get("https://tymeer.pythonanywhere.com/login")
        print(response)

    def login(self):
        """Метод, который отправляет данные логина и пароля на сервер."""
        username = self.username.text()
        password = self.password.text()
        if not username or not password:
            QMessageBox.warning(None, "Error", "Please fill in both username and password")
            return

        try:
            response = requests.get(
                "https://tymeer.pythonanywhere.com/login",
                params={"username": username, "password": password}
            )

            # Обрабатываем ответ сервера
            if response.status_code == 200:
                if self.robot_box.isChecked():
                    self.movies_window = Movies.MoviesWindow(username)
                    self.movies_window.show()
                    self.close()
                else:
                    QMessageBox.warning(None, "Error", "Пройдите проверку на робота")

                # После успешного логина можно открыть другое окно или перейти в другое состояние
            else:
                QMessageBox.warning(None, "Error", response.json().get("message", "Invalid username or password"))
        except requests.ConnectionError:
            QMessageBox.critical(None, "Error", "Could not connect to the server")

    def open_registration(self):
        self.registration_window = Registration.Registration(self)
        self.registration_window.show()
        self.hide()

    def open_movies(self):
        self.movies_window = Movies.MoviesWindow()
        self.movies_window.show()
        self.close()

def application():
    MovieAit = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(MovieAit.exec_())

if __name__ == "__main__":
    application()
    
