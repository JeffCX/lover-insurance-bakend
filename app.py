from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['GET'])
def login():
    return "hi"

@app.route('/register', methods=['GET'])
def register():
    return "hi"

@app.route('/buy-insurance', methods=['GET'])
def buy_insurance():
    return "hi"

@app.route('/get-question', methods=['GET'])
def get_question():
    return "hi"

@app.route('/select-question', methods=['GET'])
def select_question():
    return "hi"

@app.route('/update-question', methods=['GET'])
def update_question():
    return "hi"

@app.route('/claim-middle-reward', methods=['GET'])
def claim_middle_reward():
    return "hi"

@app.route('/claim-final-reward', methods=['GET'])
def claim_final_reward():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)