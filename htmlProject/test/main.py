from flask import Flask, request, render_template, jsonify, session
from flask_cors import CORS
from random import randint
from collections import defaultdict

app = Flask(__name__)
CORS(app)

app.secret_key = "aloe"

users = {}

question = ""

ops = "+-"

@app.route('/')
def mainWindow():
    return render_template("registration.html") 


@app.route('/check_user', methods=['POST'])
def checkUser():
    data = request.get_json()
    username = data.get('username')
    
    session['username'] = username
    
    if username not in users:
        users[username] = {"correct": 0,"incorrect":0,"question_count":0}
    
    return jsonify({"status": "success"}), 200


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/get_question')
def generate_question():
    try:
        first = randint(1,100)
        second = randint(1,100)
        first, second = max(first,second), min(first,second)
        op = ops[randint(0,1)]
        question = f"{first}{op}{second}"
        return jsonify({"question:": question})
    except:
        return "ERROR IN THE SERVER"
    
 
@app.route('/check_answer', methods=['POST'])
def check_answer():
        
    data = request.json
    username = session['username']
    
    if data['correct']:
        users[username]['correct']+=1
    else:
        users[username]['incorrect']+=1
    users[username]["question_count"]+=1
    
    return jsonify(users[username])


@app.route('/get_stats')
def get_stats():
    username = session.get('username', 'guest')
    if username not in users:
        users[username] = {"correct": 0, "incorrect": 0, "question_count": 0}
    
    return jsonify(users[username])


    
if __name__ == "__main__":
    app.run(debug=True)