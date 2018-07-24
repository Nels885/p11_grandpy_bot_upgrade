import time

from .bot import bot_analysis
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


@app.route('/', methods=['POST'])
def add_post():
    """
    Receives user messages and return GranpyBot answers
    :return: return the answers of GrandpyBot in JSON format
    """
    message = request.form['content']

    # Analysis of the question by GrandPy Bot
    msgs_bot = bot_analysis(message)

    # load animation test
    time.sleep(3)

    return json.dumps({'status': 'OK', 'message': msgs_bot})
