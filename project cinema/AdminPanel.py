import sys
import random, requests
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont

class AdminPanel(QMainWindow):
    def __init__(self, movie_window):
        super(AdminPanel, self).__init__()

        self.movie_window = movie_window
        self.setWindowTitle("Admin")
        self.setGeometry(690, 250, 600, 700)
        self.setFixedSize(600, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c2c2c;}
        """)

        self.movies_btn = QtWidgets.QPushButton(self)
        self.movies_btn.setFixedSize(120, 40)
        self.movies_btn.setText("Movies")
        self.movies_btn.move(20, 30)
        self.movies_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                border: 2px solid #211E1E;
                font-size: 22px;
            }
            QPushButton:hover {
                background-color: #544CAE;
                border: 2px solid #211E1E;
            }
        """)

        self.admin_txt = QtWidgets.QLabel(self)
        self.admin_txt.setText("Admin panel")
        self.admin_txt.setAlignment(QtCore.Qt.AlignCenter)  # Выравнивание текста по центру
        self.admin_txt.move(170, 40)  # Уст
        self.admin_txt.setStyleSheet("""
            QLabel{
                font-size: 40px;
                color: white;
                font-weight: bold;
            }
        """)
        self.admin_txt.adjustSize()

        self.movie_txt = QtWidgets.QLabel(self)
        self.movie_txt.setText("Movie name")
        self.movie_txt.setAlignment(QtCore.Qt.AlignCenter)  # Выравнивание текста по центру
        self.movie_txt.setFixedSize(self.width(), 50)  # Задаем фиксированную ширину равную ширине окна
        self.movie_txt.move(0, 150)  # Уст
        self.movie_txt.setStyleSheet("""
            QLabel{
                font-size: 30px;
                color: white;
            }
        """)
        self.movie_txt.adjustSize()

        self.schedule_txt = QtWidgets.QLabel(self)
        self.schedule_txt.setText("Schedule")
        self.schedule_txt.setAlignment(QtCore.Qt.AlignCenter)  # Выравнивание текста по центру
        self.schedule_txt.setFixedSize(self.width(), 50)  # Задаем фиксированную ширину равную ширине окна
        self.schedule_txt.move(0, 320)  # Уст
        self.schedule_txt.setStyleSheet("""
            QLabel{
                font-size: 30px;
                color: white;
            }
        """)
        self.schedule_txt.adjustSize()

        self.movie_LineEdit = QtWidgets.QLineEdit(self)
        self.movie_LineEdit.move(160, 230)
        self.movie_LineEdit.setFixedSize(280, 70)
        self.movie_LineEdit.setStyleSheet("""
            QLineEdit {
                font-size: 22px;
                border-radius: 6px;
                background-color: white;
                color: black;
            }
        """)

        self.schedul_LineEdit = QtWidgets.QLineEdit(self)
        self.schedul_LineEdit.move(160, 400)
        self.schedul_LineEdit.setFixedSize(280, 70)
        self.schedul_LineEdit.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                border-radius: 6px;
                background-color: white;
                color: black;
            }
        """)

        self.add_btn = QtWidgets.QPushButton(self)
        self.add_btn.setFixedSize(180, 60)
        self.add_btn.setText("Add")
        self.add_btn.move(50, 550)
        self.add_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                border: 2px solid #211E1E;
                font-size: 26px;
            }
            QPushButton:hover {
                background-color: #544CAE;
                border: 2px solid #211E1E;
            }
        """)
        self.add_btn.clicked.connect(self.add_movie)

        self.delete_btn = QtWidgets.QPushButton(self)
        self.delete_btn.setFixedSize(180, 60)
        self.delete_btn.setText("Delete")
        self.delete_btn.move(370, 550)
        self.delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #AD1B1B;
                color: white;
                border-radius: 10px;
                border: 2px solid #211E1E;
                font-size: 26px;
            }
            QPushButton:hover {
                background-color: #544CAE;
                border: 2px solid #211E1E;
            }
        """)
        self.delete_btn.clicked.connect(self.delete_movie)
        self.movies_btn.clicked.connect(self.back)
        

    def add_movie(self):
        title = self.movie_LineEdit.text()
        time = self.schedul_LineEdit.text()
        if not title or not time:
            QMessageBox.warning(self, "Error", "Please fill in both title and time")
            return

        try:
            response = requests.get(
                "https://tymeer.pythonanywhere.com/admin_add",
                params={"title": title, "time": time}
            )
            print(f"Response: {response.status_code}, Data: {response.text}")

            if response.status_code == 200:
                try:
                    data = response.json()
                    if data is False:
                        QMessageBox.warning(self, "Error", "Movie already exists or time for this movie already exist")
                    elif data is True:
                        QMessageBox.information(self, "Success", f"Movie {title} added successfully")
                    else:
                        QMessageBox.warning(self, "Error", "Unexpected response from server")
                except ValueError:
                    QMessageBox.warning(self, "Error", "Invalid response from server")
            else:
                QMessageBox.warning(self, "Error", "Server error: " + response.reason)
        except requests.ConnectionError:
            QMessageBox.critical(self, "Error", "Could not connect to the server")

    def delete_movie(self):
        title = self.movie_LineEdit.text()
        time = self.schedul_LineEdit.text()
        if not title:
            QMessageBox.warning(self, "Error", "Please fill title")
            return

        try:
            response = requests.get(
                "https://tymeer.pythonanywhere.com/admin_delete",
                params={"title": title, "time": time}
            )

            if response.status_code == 200:
                try:
                    data = response.json()
                    if data is False:
                        QMessageBox.warning(self, "Error", "Movie doesn't exist")
                    elif data is True:
                        QMessageBox.information(self, "Success", f"Movie {title} deleted successfully")
                    else:
                        QMessageBox.warning(self, "Error", "Unexpected response from server")
                except ValueError:
                    QMessageBox.warning(self, "Error", "Invalid response from server")
            else:
                QMessageBox.information(self, 'Success', 'You successfully deleted whole movie')
        except requests.ConnectionError:
            QMessageBox.critical(self, "Error", "Could not connect to the server")

    def back(self):
        self.movie_window.show()
        self.close()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    from Movies import Movies  # Импортируем MoviesWindow из отдельного файла

    app = QApplication(sys.argv)
    movies_window = Movies()
    movies_window.show()
    sys.exit(app.exec_())
