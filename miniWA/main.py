# import os
# import sqlite3
# from flask import Flask, request, render_template, session, redirect, url_for, flash
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# app.secret_key = "aloe"

# def get_db_connection():
#     conn = sqlite3.connect('db/database.db')
#     conn.row_factory = sqlite3.Row
#     return conn   
    
# @app.route('/')
# def loginWindow():
#     return render_template("login.html")

# @app.route('register', method=['GET', 'POST'])
    

# if __name__ == "__main__":
#     app.run(debug=True)


import os
import sqlite3
from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = "aloe"

# Функция для получения соединения с БД
def get_db_connection():
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def loginWindow():
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("registration.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Дополнительно можно добавить валидацию password2, если потребуется

        conn = get_db_connection()
        cursor = conn.cursor()
        # Проверяем, существует ли уже пользователь с таким именем
        cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash("Пользователь с таким именем уже существует!")
            conn.close()
            return redirect(url_for('register'))
        else:
            cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            flash("Регистрация прошла успешно! Теперь можете авторизоваться.")
            return redirect(url_for('loginWindow'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        session['user'] = username
        return render_template("chat.html")
    else:
        flash("Неверное имя пользователя или пароль")
        return redirect(url_for('loginWindow'))

# Создание таблицы, если её ещё нет
with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"""
    cursor.execute(query)

if __name__ == "__main__":
    app.run(debug=True)
