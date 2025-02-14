from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys, requests


class BookSeats(QMainWindow):
    def __init__(self, movies_window, username):
        super(BookSeats, self).__init__()
        self.movies_window = movies_window
        self.username = username

        self.setWindowTitle(f"Book Seats - {username}")
        self.setFixedSize(900, 700)
        self.setGeometry(540, 250, 900, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c2c2c
            }
        """)

        self.selected_seats = []  # Список выбранных мест

        self.selected_seats_text = QtWidgets.QLabel(self)
        self.selected_seats_text.setText(f"Выбранные места : ")
        self.selected_seats_text.setGeometry(100, 510, 900, 30)
        self.selected_seats_text.setStyleSheet("""
            QLabel {
                color : white;
                font-size : 14px ;}""")

        # Кнопка "Купить"

        self.buy_btn = QtWidgets.QPushButton(self)
        self.buy_btn.setText("Buy")
        self.buy_btn.setGeometry(375, 600, 150, 50)
        self.buy_btn.setStyleSheet("""
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
        self.buy_btn.clicked.connect(self.back_to_movies)

        self.booked_seats = []  # Забронированные места
        self.get_booked_seats_from_server()
        self.init_ui()

        # Метка для экрана
        self.screen = QtWidgets.QLabel(self)
        self.screen.setText("S C R E E N")
        self.screen.setFixedSize(600, 20)
        self.screen.setAlignment(QtCore.Qt.AlignCenter)
        self.screen.move((self.width() - self.screen.width()) // 2, 550)
        self.screen.setStyleSheet("""
            QLabel {
                color: black;
                font-size: 14px;
                border-radius: 10px;
                background-color: white;
            }
        """)

        self.movies_btn = QtWidgets.QPushButton(self)
        self.movies_btn.move(10, 18)
        self.movies_btn.setText("Back To Movies")
        self.movies_btn.setFixedSize(140, 40)
        self.movies_btn.setStyleSheet("""
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
        self.movies_btn.clicked.connect(self.back_to_movie)


    def init_ui(self):
        # Определяем размеры кнопок
        button_width, button_height = 60, 40
        # Начальные координаты для размещения сидений
        start_x, start_y = 90, 100
        # Расстояние между кнопками
        spacing_x, spacing_y = 15, 20

        # Абсолютное размещение кнопок
        for row in range(7):  # Строки
            for col in range(10):  # Колонки
                x = start_x + col * (button_width + spacing_x)
                y = start_y + row * (button_height + spacing_y)

                seat_btn = QtWidgets.QPushButton(self)
                seat_btn.setGeometry(x, y, button_width, button_height)
                seat_btn.setProperty("position", (row, col))

                # Устанавливаем цвет в зависимости от состояния
                if (row, col) in self.booked_seats:
                    seat_btn.setStyleSheet("background-color: black;")
                    seat_btn.setEnabled(False)
                else:
                    seat_btn.setStyleSheet("background-color: green;")
                    seat_btn.clicked.connect(self.book_seat)

        # Добавляем метки для рядов (буквы)
        for row in range(7):
            label = QtWidgets.QLabel(self)
            label.setText(chr(65 + row))  # A, B, C, ...
            label.setStyleSheet("color: white; font-size: 14px;")
            label.setGeometry(start_x - 30, start_y + row * (button_height + spacing_y), 20, 40)
        # Добавляем метки для колонок (цифры)
        for col in range(10):
            label = QtWidgets.QLabel(self)
            label.setText(str(col + 1))  # 1, 2, 3, ...
            label.setStyleSheet("color: white; font-size: 14px;")
            label.setGeometry(start_x + col * (button_width + spacing_x) + 23, start_y - 40, 20, 40)

    def book_seat(self):
        button = self.sender()
        row, col = button.property("position")
        seat_name = f"{chr(65 + row)}{col + 1}"  # Преобразуем в формат A1, B2 и т.д.
        current_style = button.styleSheet()
        if "background-color: green" in current_style:
            button.setStyleSheet("background-color: red;")
            self.selected_seats.append(seat_name)
        elif "background-color: red" in current_style:
            button.setStyleSheet("background-color: green;")
            self.selected_seats.remove(seat_name)
        self.selected_seats_text.setText(f"Выбранные места : {', '.join(self.selected_seats)}")


    def get_booked_seats_from_server(self):
        try:
            movie_title = self.movies_window.movies_list.currentItem().text()
            movie_time = self.movies_window.time_list.currentItem().text()
            print(f"Requesting booked seats for movie: {movie_title}, time: {movie_time}")  # Отладочное сообщение
        except AttributeError as e:
            print(f"Error accessing movies_window attributes: {e}")
            return

        try:
            response = requests.get(
                "https://tymeer.pythonanywhere.com/get_booked_seats",
                params={"title": movie_title, "time": movie_time}
            )
            print(f"Response status code: {response.status_code}")  # Отладочное сообщение
            print(f"Response content: {response.content}")  # Отладочное сообщение
            booked_seats = response.json()
            if response.status_code == 200:
                try:
                    for seat in booked_seats:
                        for single_seat in seat.split(','):  # Разделяем строку на отдельные места
                            col = ord(single_seat[0]) - 65  # Преобразуем букву в индекс строки
                            row = int(single_seat[1:]) - 1  # Преобразуем номер места в индекс колонки
                            self.booked_seats.append((col, row))
                            print(f"Booked seat added: {single_seat}")  # Отладочное сообщение
                except Exception as e:
                    print(f"Error processing seats: {e}")  # Отладочное сообщение
        except requests.ConnectionError as e:
            print(f"Connection error: {e}")
            QMessageBox.critical(self, "Error", "Could not connect to the server")

    def back_to_movie(self):
        self.movies_window.show()
        self.close()

    def back_to_movies(self):
        if len(self.selected_seats) > 0:
            movie_title = self.movies_window.movies_list.currentItem().text()
            movie_time = self.movies_window.time_list.currentItem().text()

            # Отправляем забронированные места на сервер
            self.update_movie_seats(movie_title, movie_time)
            self.selected_seats_text.setText("Выбранные места : ")

            # Обновляем кнопки для забронированных мест
            self.init_ui()

            self.movies_window.show()
            self.close()

    def update_movie_seats(self, movie_title, movie_time):
        # Отправляем выбранные места на сервер
        seats_str = ','.join(self.selected_seats)  # Преобразуем список мест в строку
        response = requests.get(
            "https://tymeer.pythonanywhere.com/update_movie_seats",
            params={"title": movie_title, "time": movie_time, "seats": seats_str, "username": self.username}
        )
        print(f"Response status code: {response.status_code}")  # Отладочное сообщение
        print(f"dan: {response.text}")  # Отладочное сообщение
        try:
            if response.status_code == 200:
                print("Seats successfully updated.")
            else:
                print("Error while updating seats.")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Предполагается, что movies_window передается из другого места
    movies_window = None  # Замените на реальный объект movies_window
    book_seats_window = BookSeats(movies_window)
    book_seats_window.show()
    sys.exit(app.exec_())