from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "aloe"

def init_db():
    db = sqlite3.connect('users.db')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )""")
    db.commit()
    db.close()

init_db()

@app.route('/')
def loginPage():
    return render_template("login.html")

@app.route('/registration')
def registrationPage():
    return render_template("registration.html")

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"success": False , "message": "Заполните все поля"})

    try:
        db = sqlite3.connect('users.db')
        cursor = db.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ?", (username))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({"success": False, "message": "Пользователь уже существует"})
        
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.close()
        return jsonify({"success": True, "message":"Регистрация успешна"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
        
if __name__ ==  "__main__":
    app.run(debug=True)
    
