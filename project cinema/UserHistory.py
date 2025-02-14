from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys, requests

class UserHistory(QMainWindow):
    def __init__(self, movie_window, username):
        super(UserHistory, self).__init__()

        self.movie_window = movie_window
        self.username = username
        self.setWindowTitle("User History")
        self.setGeometry(510, 250, 900, 700)
        self.setFixedSize(900, 700)
        self.setStyleSheet("""
            QMainWindow{
                background-color: #2c2c2c
                }""")

        # Создаем таблицу
        self.history_table = QTableWidget(self)
        self.history_table.setFixedSize(850, 500)
        self.history_table.move(20, 20)
        self.history_table.setStyleSheet("""
            QTableWidget {
                background-color: white;
                color: black;
                border-radius: 10px;
                font-size: 16px;
                border: 2px solid;
            }
            QHeaderView::section {
                background-color: #808080; /* Серый цвет */
                color: white;
                font-size: 16px;
            }
        """)

        # Устанавливаем количество колонок
        self.history_table.setColumnCount(3)  # Три колонки: Movie, Time, Seat

        # Устанавливаем заголовки
        self.history_table.setHorizontalHeaderLabels(["Movie", "Time", "Seat"])
        # Устанавливаем фиксированные размеры колонок
        self.history_table.setColumnWidth(0, 200)  # Ширина колонки "Movie"
        self.history_table.setColumnWidth(1, 150)  # Ширина колонки "Time"
        self.history_table.setColumnWidth(2, 497)  # Ширина колонки "Seat"

        # Устанавливаем фиксированную высоту строк
        self.history_table.verticalHeader().setDefaultSectionSize(50)  # Высота каждой строки

        # Загружаем историю пользователя
        self.load_history()

        # Кнопка "Movies"
        self.movies_btn = QtWidgets.QPushButton(self)
        self.movies_btn.setText("Movies")
        self.movies_btn.setFixedSize(150, 50)
        self.movies_btn.move(375, 630)
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
        self.movies_btn.clicked.connect(self.back)

    def load_history(self):
        try:
            response = requests.get("https://tymeer.pythonanywhere.com/user_history",
                                    params={"username": self.username})
            if response.status_code == 200:
                history_data = response.json()
                self.history_table.setRowCount(0)  # Очищаем таблицу
                for title, times in history_data.items():
                    for time, seats in times.items():
                        row_position = self.history_table.rowCount()
                        self.history_table.insertRow(row_position)
                        self.history_table.setItem(row_position, 0, QTableWidgetItem(title))  # Название фильма
                        self.history_table.setItem(row_position, 1, QTableWidgetItem(time))  # Время
                        self.history_table.setItem(row_position, 2,
                                                   QTableWidgetItem(", ".join(seats)))  # Места, объединённые запятой
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Failed to load history.")
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Error", "Cannot connect to the server.")

    def back(self):
        self.movie_window.show()
        self.close()

def application():
    app = QApplication(sys.argv)
    # Предполагается, что movies_window передается из другого места
    movies_window = None  # Замените на реальный объект movies_window
    userhistory = UserHistory(movies_window, "test_username")  # Замените "test_username" на реальное имя пользователя
    userhistory.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
