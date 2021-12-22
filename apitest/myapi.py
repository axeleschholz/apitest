from flask import Flask
from flask import jsonify
from flask import request
import random

api = Flask(__name__)


# http://localhost:5000/
@api.route("/")
def helloWorld():
    print("api was hit")
    return jsonify({'statement': 'Hello, world!'})

# http://localhost:5000/question?body=meaningoflife


@api.route("/question")
def hello():
    question = request.args.get('body')
    print("Recieved query " + question)
    answers = ["Yes", "No", "Maybe", "42"]
    return jsonify({'answer': random.choice(answers)})


api.run()
