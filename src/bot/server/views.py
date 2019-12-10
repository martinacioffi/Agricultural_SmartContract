from flask import render_template, redirect, url_for, request, Blueprint
from src.bot.create_chatbot.helpers import detect_intent_texts
from src.contract import create_contract
from src.contract import create_new_address
import os

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


@home_blueprint.route('/')
def welcome():
    return render_template('index.html')


pacman_blueprint = Blueprint(
    'pacman', __name__,
    template_folder='templates'
)


@pacman_blueprint.route('/get')
def process():
    session = 'new_session'
    raw_query = request.args.get('msg')
    if raw_query is None:
        return redirect(url_for('home.welcome'))
    elif raw_query.upper() == 'PROCEED':

        location = 'milan'  #TODO get this from bot parameters
        month = 4 #todo same from session vars
        precip = 32 #todo again
        address = create_new_address()
        _, __, ___, _____, utterance = create_contract(location, month, precip, address)
        return utterance
    else:
        bot_responses = ''
        action, bot_response, params = detect_intent_texts(os.environ['PROJECT_ID'], session, raw_query)
        if action.startswith('smalltalk'):
            bot_responses = f'{bot_response}<br><br>{bot_responses}'
        else:
            bot_responses += f'{bot_response}<br>'
        bot_responses = str(bot_responses)
        return bot_responses
