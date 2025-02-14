from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget, QListWidgetItem, QMessageBox
import sys
import UserHistory, MovieInfo, AdminPanel, BookSeat
import requests

class MoviesWindow(QMainWindow):
    def __init__(self, username):
        super(MoviesWindow, self).__init__()
        self.username = username

        self.setWindowTitle("Movies")
        self.setGeometry(540, 250, 900, 700)
        self.setFixedSize(900, 700)  # Устанавливаем фиксированный размер окна

        # Устанавливаем черный фон окна с помощью QPalette
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.black)
        self.setPalette(palette)

        # Создаем виджет для фона
        self.background_label = QLabel(self)
        self.background_label.setGeometry(self.rect())
        self.background_label.setPixmap(QtGui.QPixmap('.\images\photokino.jpg').scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.background_label.setScaledContents(True)

        # Применяем эффект прозрачности
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.4)  # 50% прозрачности
        self.background_label.setGraphicsEffect(self.opacity_effect)

        # Title
        self.title_label = QLabel("Movies", self)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 34px;
                font-weight: bold;
            }
        """)
        self.title_label.adjustSize()
        self.title_label.move(390, 20)

        # Movies list
        self.movies_list = QListWidget(self)
        self.movies_list.setStyleSheet("""
            QListWidget {
                background-color: white;
                color: black;
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
                border: 2px solid #211E1E;
            }
        """)
        self.movies_list.setFixedSize(300, 300)
        self.movies_list.move(80, 80)
        self.movies = []
        for movie in self.movies:
            item = QListWidgetItem(movie)
            self.movies_list.addItem(item)

        # Time list
        self.time_list = QListWidget(self)
        self.time_list.setStyleSheet("""
            QListWidget {
                background-color: white;
                color: black;
                border-radius: 10px;
                padding: 5px;
                font-size: 16px;
                border: 2px solid #211E1E;
            }
        """)
        self.time_list.setFixedSize(300, 300)
        self.time_list.move(520, 80)

        self.movie_times = {}

        # Admin panel button
        self.admin_panel_btn = QPushButton("Admin panel", self)
        self.admin_panel_btn.setStyleSheet("""
            QPushButton {
                background-color: #211E1E;
                color: white;
                border-radius: 10px;
                border: 2px solid #3e8e41;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #544CAE;
                border: 2px solid #211E1E;
            }
        """)
        self.admin_panel_btn.setFixedSize(150, 40)
        self.admin_panel_btn.move(700, 20)
        self.admin_panel_btn.clicked.connect(self.open_admin)

        # Seats button
        self.seats_btn = QPushButton("Seats", self)
        self.seats_btn.setStyleSheet("""
            QPushButton {
                background-color: #211E1E;
                color: white;
                border-radius: 10px;
                border: 2px solid #3e8e41;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #544CAE;
                border: 2px solid #211E1E;
            }
        """)
        self.seats_btn.setFixedSize(180, 60)
        self.seats_btn.move(360, 420)
        self.seats_btn.setEnabled(False)
        self.seats_btn.clicked.connect(self.open_seats) # Делаем кнопку неактивной

        # Подключаем события выбора фильма и времени
        self.movies_list.itemSelectionChanged.connect(self.check_seats_button)
        self.time_list.itemSelectionChanged.connect(self.check_seats_button)
        self.movie_info_btn = QPushButton("Movie Info", self)
        self.movie_info_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                border: 2px solid #211E1E;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
                border: 2px solid #211E1E;
            }
        """)
        self.movie_info_btn.setFixedSize(180, 60)
        self.movie_info_btn.move(360, 500)
        self.movie_info_btn.clicked.connect(self.open_movie_info)

        # User history button
        self.user_history_btn = QPushButton("User History", self)
        self.user_history_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                border: 2px solid #211E1E;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
                border: 2px solid #211E1E;
            }
        """)
        self.user_history_btn.setFixedSize(180, 60)
        self.user_history_btn.move(360, 580)
        self.user_history_btn.clicked.connect(self.open_user_history)

        self.update_btn = QPushButton("Update", self)
        self.update_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #4CAF50;
                        color: white;
                        border-radius: 10px;
                        border: 2px solid #211E1E;
                        font-size: 16px;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color: #45a049;
                        border: 2px solid #211E1E;
                    }
                """)
        self.update_btn.setFixedSize(150, 40)
        self.update_btn.move(50, 25)
        self.update_btn.clicked.connect(self.load_movies)
        self.movies_list.itemClicked.connect(self.show_movie_times)

    def check_seats_button(self):
        """Активирует кнопку Seats только если выбраны фильм и время."""
        if self.movies_list.currentItem() and self.time_list.currentItem():
            self.seats_btn.setEnabled(True)
        else:
            self.seats_btn.setEnabled(False)

    def show_movie_times(self, item):
        selected_movie = item.text()
        try:
            response = requests.get(
                "https://tymeer.pythonanywhere.com/get_movies_time",
                params={"title": selected_movie}
            )
            print(f"Response: {response.status_code}, Data: {response.text}")
            movies_times = response.json()
            if response.status_code == 200:
                try:
                    self.time_list.clear()
                    for time in movies_times:
                        self.time_list.addItem(QListWidgetItem(time))
                    self.time_list.show()
                except ValueError:
                    QMessageBox.warning(self, "Error", "Invalid response from server")
        except requests.ConnectionError:
            QMessageBox.critical(self, "Error", "Could not connect to the server")

    def showEvent(self, event):
        """Обновление списка фильмов и времени при каждом открытии окна."""
        self.load_movies()
        super().showEvent(event)

    def load_movies(self):
        try:
            response = requests.get("https://tymeer.pythonanywhere.com/get_movies")
            if response.status_code == 200:
                movies_data = response.json()
                self.movies_list.clear()
                self.time_list.clear()
                for title, times in movies_data.items():
                    self.movies_list.addItem(QListWidgetItem(title))
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Failed to load movies.")
        except requests.ConnectionError:
            QtWidgets.QMessageBox.critical(self, "Error", "Cannot connect to the server.")

    def open_user_history(self):
        self.user_history_window = UserHistory.UserHistory(self, self.username)
        self.user_history_window.show()
        self.hide()

    def open_movie_info(self):
        # Получаем выбранный фильм и время
        selected_movie = self.movies_list.currentItem()
        selected_time = self.time_list.currentItem()

        if not selected_movie:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a movie.")
            return

        movie_title = selected_movie.text()
        movie_time = selected_time.text() if selected_time else None

        # Передаем данные вместо объекта окна
        self.movie_info_window = MovieInfo.MovieInfo(self, self.username, movie_title, movie_time)
        self.movie_info_window.show()
        self.hide()

    def open_admin(self):
        self.admin_panel_window = AdminPanel.AdminPanel(self)
        self.admin_panel_window.show()
        self.hide()

    def open_seats(self):
        print("Opening Seats window")  # Отладочное сообщение
        self.seats_window = BookSeat.BookSeats(self, self.username)
        self.seats_window.show()
        self.hide()

def application():
    app = QApplication(sys.argv)
    movies_window = MoviesWindow("test_username")  # Замените "test_username" на реальное имя пользователя
    movies_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
