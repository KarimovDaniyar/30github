from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
import sys, requests

class MovieInfo(QMainWindow):
    def __init__(self, parent_window, username, movie_title, movie_time):
        super(MovieInfo, self).__init__()

        self.parent_window = parent_window
        self.username = username
        self.movie_title = movie_title
        self.movie_time = movie_time

        self.setWindowTitle("Movie Info")
        self.setGeometry(540, 250, 900, 700)
        self.setFixedSize(900, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c2c2c;
            }
            QLabel {
                color: lightgray;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border: 2px solid #211E1E;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QTableWidget {
                background-color: #e0e0e0;
                color: black;
                font-size: 14px;
                border: 2px solid #999;
                border-radius: 5px;
            }
            QHeaderView::section {
                background-color: #d3d3d3;
                color: black;
                font-size: 14px;
                font-weight: bold;
                border: 1px solid #aaa;
            }
        """)

        # Название фильма
        self.movie_label = QLabel(self)
        if self.movie_time:
            self.movie_label.setText(f"{self.movie_title} - {self.movie_time}")
        else:
            self.movie_label.setText(self.movie_title)
        self.movie_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 36px;
                font-weight: bold;
            }
        """)
        self.movie_label.adjustSize()
        self.movie_label.move(380, 5)

        # Quantity label
        self.quantity_label = QLabel("Quantity: 0       ", self)
        self.quantity_label.move(20, 40)
        self.quantity_label.setStyleSheet("""
            QLabel {
                color: #2c2c2c;
                font-size: 36px;
                font-weight: bold;
                background-color: white;
                border-radius: 10px;
                padding: 1px 1px;
                min-width: 1px;
            }
        """)
        self.quantity_label.adjustSize()

        # Seans label
        self.seans_label = QLabel("Seans: 0   ", self)
        self.seans_label.setStyleSheet("""
            QLabel {
                color: #2c2c2c;
                font-size: 36px;
                font-weight: bold;
                background-color: white;
                border-radius: 10px;
                padding: 1px 1px;
                min-width: 5px;
            }
        """)
        self.seans_label.adjustSize()
        self.seans_label.move(20, 90)

        # People label
        self.people_label = QLabel("People:", self)
        self.people_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 36px;
                font-weight: bold;
            }
        """)
        self.people_label.adjustSize()
        self.people_label.move(20, 150)

        # People table
        self.people_table = QTableWidget(self)
        self.people_table.setColumnCount(2)
        self.people_table.setHorizontalHeaderLabels(["Name", "Time"])
        self.people_table.horizontalHeader().setStretchLastSection(True)
        self.people_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.people_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.people_table.setRowCount(0)
        self.people_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.people_table.setFixedSize(550, 450)
        self.people_table.move(20, 220)

        # Movies button
        self.movies_btn = QPushButton("Movies", self)
        self.movies_btn.setFixedSize(200, 70)
        self.movies_btn.move(650, 600)
        self.movies_btn.clicked.connect(self.back)

        self.movie_info()

    def movie_info(self):
        try:
            # Запрашиваем информацию о фильме
            response = requests.get(
                "https://tymeer.pythonanywhere.com/movie_info",
                params={"title": self.movie_title, "time": self.movie_time}
            )
            if response.status_code != 200:
                raise Exception(f"Invalid response: {response.status_code}")
            data = response.json()
            movie_data = data.get("movie_data", {})
            total_seats = data.get("total_seats", 0)
            total_seans = data.get("total_seans", 0)

            print(total_seats)

            # Обновляем данные таблицы
            self.people_table.setRowCount(0)
            row_position = 0
            for user, times in movie_data.items():
                for time in times:
                    if self.movie_time is None or time == self.movie_time:
                        self.people_table.insertRow(row_position)
                        self.people_table.setItem(row_position, 0, QTableWidgetItem(user))
                        self.people_table.setItem(row_position, 1, QTableWidgetItem(time))
                        row_position += 1

            # Обновляем метки
            if self.movie_time is None:
                self.quantity_label.setText(f"Quantity: {total_seats}")
                self.seans_label.setText(f"Seans: {total_seans}")
            else:
                self.quantity_label.setText(f"Quantity: {total_seats}")
                self.seans_label.setText(f"Seans: 1")

        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.information(self, "Error", "Failed to load movie info")

    def back(self):
        self.parent_window.show()
        self.close()

def application():
    app = QApplication(sys.argv)

    # Замените эти значения на реальные
    parent_window = None  # Если нет родительского окна, используйте None
    username = "test_user"  # Имя пользователя
    movie_title = "Movie1"  # Название фильма
    movie_time = "18:30"  # Время показа фильма

    movie_details_window = MovieInfo(parent_window, username, movie_title, movie_time)
    movie_details_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
