from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox, QLabel
import sys
import requests


class Registration(QMainWindow):
    def __init__(self,login_window):
        super(Registration, self).__init__()
        self.login_window = login_window

        self.setWindowTitle("Create Account")
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
            QtGui.QPixmap('.\images\macFront1.jpg').scaled(self.size(), QtCore.Qt.KeepAspectRatio,
                                                          QtCore.Qt.SmoothTransformation))
        self.background_label.setScaledContents(True)

        # Применяем эффект прозрачности
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.4)  # 50% прозрачности
        self.background_label.setGraphicsEffect(self.opacity_effect)
    
        self.reg_text = QtWidgets.QLabel(self)
        self.reg_text.setText("Create Account")
        self.reg_text.move(108,20)
        self.reg_text.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
                font-family: 'Arial Black', Gadget, sans-serif;
            }
        """)
        self.reg_text.adjustSize()
        
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
        self.password.move(75, 120)
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
        
        self.r_password = QtWidgets.QLineEdit(self)
        self.r_password.setFixedSize(200, 40)
        self.r_password.move(75, 200)
        self.r_password.setPlaceholderText("Confirm Password")
        self.r_password.setEchoMode(QLineEdit.Password)
        self.r_password.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                border-radius: 6px;
                background-color: rgba(255, 255, 255, 0.4);  /* Белый фон с прозрачностью */
                color: black;  /* Цвет текста */
                padding-left: 8px;
                border: 2px solid #211E1E;  /* Обводка */
            }
        """)

        self.signup_btn = QtWidgets.QPushButton(self)
        self.signup_btn.move(112, 290)
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
        self.signup_btn.clicked.connect(self.register)
        self.login_btn = QtWidgets.QPushButton(self)
        self.login_btn.move(112, 365)
        self.login_btn.setText("Back To Login")
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
        self.login_btn.clicked.connect(self.back_to_login)
    def back_to_login(self):
        self.login_window.show()
        self.close()

    def register(self):
        """Метод, который отправляет данные логина и пароля на сервер."""
        username = self.username.text()
        password = self.password.text()
        conf_password = self.r_password.text()
        if not username or not password:
            QMessageBox.warning(None, "Error", "Please fill in both username and password")
            return
        if len(password) < 5:
            QMessageBox.warning(None, "Error", "Password cannot be less 5 letters")
            return

        try:
            if password == conf_password:
                response = requests.get(
                    "https://tymeer.pythonanywhere.com/register",  # Замените на URL вашего приложения Flask
                    params={"username": username, "password": password}
                )

            # Обрабатываем ответ сервера
                if response.status_code == 200:
                    print(response.text)
                    if response.json() == False:
                        QMessageBox.warning(None, "Error", "User already exist")
                    else:
                        QMessageBox.information(None, "Succes", "Вы успешно зарегистроровались")
                        self.login_window.show()
                        self.close()
                else:
                    QMessageBox.warning(None, "Error", response.json().get("message", "Invalid username or password"))
            else:
                QMessageBox.warning(None, "Error", "Not same password")

        except requests.ConnectionError:
            QMessageBox.critical(None, "Error", "Could not connect to the server")


        
      

def application():
    MovieAit = QApplication(sys.argv)
    login = Registration()
    login.show()
    sys.exit(MovieAit.exec_())

if __name__ == "__main__":
    application()