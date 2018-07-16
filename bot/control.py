import time
from .models import *
from flask import Flask, render_template, request, json, url_for

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


@app.route('/', methods=['POST'])
def addpost():
    """
    Receives user messages and return GranpyBot answers
    :return: return the answers of GrandpyBot in JSON format
    """

    obj = KillParser('bot/static/files/fr.json')
    message = request.form['content']

    msgBot = obj.msg_analysis(message)

    # load animation test
    time.sleep(3)

    return json.dumps({'status': 'OK', 'message': msgBot})
