def movie_info(self):
    if not self.movies_window.movies_list.currentItem() or not self.movies_window.time_list.currentItem():
        QMessageBox.warning(self, "Warning", "Please select a movie and time.")
        return

    movie_title = self.movies_window.movies_list.currentItem().text()
    movie_time = self.movies_window.time_list.currentItem().text()
    try:
        response = requests.get(
            "https://tymeer.pythonanywhere.com/movie_info",
            params={"title": movie_title, "time": movie_time}
        )
        if response.status_code != 200:
            raise Exception(f"Invalid response: {response.status_code}")

        user_info = response.json()
        print(user_info)

        # Обновляем массив people_data
        self.people_data = [
            (user, time) for user, time in user_info[movie_title][movie_time].items()
            if user and time
        ]

        # Обновляем метки
        self.movie_label.setText(movie_title)
        self.quantity_label.setText(f" {len(self.people_data)}")
        self.seans_label.setText(f" {len(user_info[movie_title])}")

        # Обновляем таблицу
        self.people_table.setRowCount(0)  # Очистить таблицу
        for row, (name, time) in enumerate(self.people_data):
            self.people_table.insertRow(row)
            self.people_table.setItem(row, 0, QTableWidgetItem(name))
            self.people_table.setItem(row, 1, QTableWidgetItem(time))

    except Exception as e:
        QMessageBox.information(self, "Error", f"Failed to retrieve movie info: {e}")