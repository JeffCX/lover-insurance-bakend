from flask import Flask
# import json
from flask import  request

from flask_cors import CORS
# import jsonify
app = Flask(__name__)
CORS(app)

q_list = ["1" ,"2" ,"3"]
rows, cols = (len(q_list), 2)
qa_list = [[0 for i in range(cols)] for j in range(rows)]
for i in range(len(q_list)):
    qa_list[i][0] = q_list[i]
    # qa_list[i][1]=[]

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
    return {
        "result": q_list
    }

@app.route('/update-question', methods=['GET'])
def update_question():
    idx=request.args["idx"]
    idx=int(idx)
    return {
        "result": q_list[idx]
    }

@app.route('/get_answer', methods=['GET'])
def get_answer():
    idx=request.args["idx"]
    ans=request.args["ans"]
    idx=int(idx)
    qa_list[idx][1] = ans
    return{

        "result": qa_list
    }


@app.route('/claim-middle-reward', methods=['GET'])
def claim_middle_reward():
    return "hi"

@app.route('/claim-final-reward', methods=['GET'])
def claim_final_reward():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)
