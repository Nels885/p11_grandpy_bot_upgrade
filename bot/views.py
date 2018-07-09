from .models import *
from flask import Flask, render_template, request, json

app = Flask(__name__)


app.config.from_object('config')


@app.route('/')
@app.route('/index/')
def index():
    """
    home page
    :return: index.html
    """
    return render_template('index.html')


@app.route('/post/', methods=['POST'])
def addpost():
    """
    Receives user messages and return GranpyBot answers
    :return: return the answers of GrandpyBot in JSON format
    """
    message = request.form['content']
    msgBot = ["Je ne comprends pas la question !!"]
    for msg, answers in answerBot.items():
        if message == msg:
            msgBot = answers
    return json.dumps({'status': 'OK', 'message': msgBot})
