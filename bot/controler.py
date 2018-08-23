import time
import logging as log

from flask import Flask, render_template, request, json

from .grandpybot import grandpy_bot

app = Flask(__name__)


app.config.from_object('config')

if app.debug is True:
    log.basicConfig(level=log.INFO)


@app.route('/')
@app.route('/index/')
def index():
    """
    home page
    :return: index.html
    """
    return render_template('index.html')


@app.route('/', methods=['POST'])
def msg_bot():
    """
    Receives user messages and return GranpyBot answers
    :return: return the answers of GrandpyBot in JSON format
    """
    answer = request.form['content']

    # Analysis of the question by GrandPy Bot
    answers_bot, location = grandpy_bot(answer)

    # load animation test
    time.sleep(2)

    return json.dumps({'status': 'OK',
                       'answers': answers_bot,
                       'geoLocation': location,
                       'urlApiWiki': app.config["WIKI_URL_JS"],
                       'dataSearch': app.config["WIKI_PARA_SEARCH"],
                       'dataPageId': app.config["WIKI_PARA_PAGE_ID"]
                       })

