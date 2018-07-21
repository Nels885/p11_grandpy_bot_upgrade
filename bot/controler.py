import time
from .parser import *
from .package.mediawiki import data_extract

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
def add_post():
    """
    Receives user messages and return GranpyBot answers
    :return: return the answers of GrandpyBot in JSON format
    """
    message = request.form['content']
    msgs_bot = []

    # Parsing of user's message
    pars = Parser(app.config['STOP_WORDS_JSON'], message)
    msg_bot, key_words = pars.msg_analysis()

    # search with keywords using google map and mediawiki APIs
    if len(key_words) != 0:
        msgs_bot.append(msg_bot + " La voici : 7 cité Paradis, 75010 Paris.")

        citation = data_extract("cité Paradis, Paris")
        print(citation)
        info_bot = "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? " + citation
        msgs_bot.append(info_bot)
    else:
        msgs_bot.append(msg_bot)

    # load animation test
    time.sleep(3)

    return json.dumps({'status': 'OK', 'message': msgs_bot})
