from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from random import randint
from collections import defaultdict

app = Flask(__name__)
CORS(app)

users = defaultdict()
users = {"den": {"correct": 0,
    "attempt": 0,
    "incorrect":0,
    "question_count":0} }
print(users)

d = {
    "question":"",
}

ops = "+-"

@app.route('/get_question')
def generate_question():
    try:
        first = randint(1,100)
        second = randint(1,100)
        first, second = max(first,second), min(first,second)
        op = ops[randint(0,1)]
        d["question"] = f"{first}{op}{second}"
        users["den"]["question_count"]+=1
        return jsonify({"question: ": d["question"]})
    except:
        return "ERROR IN THE SERVER"
    
@app.route('/check_result')
def check_result():
    try:
        answer = int(request.args.get("answer"))
        users["d"]["attempt"] += 1
        if answer == eval(d["question"]):
            users['den']["correct"]+=1
        else:
            users['den']["incorrect"]+=1
        return jsonify(d)
    except:
        return "ERROR IN THE SERVER"
    
@app.route('/')
def mainWindow():
    return render_template("registration.html") 
    
@app.route('/check_user', methods=['POST'])
def checkUser():
    data = request.get_json()
    username = data.get('username')
    
    if username in users:
        return jsonify({"status": "success"})
    else:
        users[username] = {"correct": 0,"attempt": 0,"incorrect":0,"question_count":0}
        return jsonify({"status": "success"}), 404

@app.route('/index')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)