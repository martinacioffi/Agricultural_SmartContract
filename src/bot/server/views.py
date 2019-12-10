from flask import render_template, redirect, url_for, request, Blueprint
from src.bot.create_chatbot.helpers import detect_intent_texts, get_params
from src.contract import create_contract
from src.contract import create_new_address
from src.weather.get_weather import avg_precipitation
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
    elif raw_query.upper() == 'CONFIRM':
        location, month = get_params(os.environ['PROJECT_ID'], session, raw_query)
        precip = avg_precipitation(location, month)
        address = create_new_address()
        _, __, ___, _____, utterance = create_contract(location, month, precip, address)
        return utterance
    else:
        bot_responses = ''
        action, bot_response = detect_intent_texts(os.environ['PROJECT_ID'], session, raw_query)
        if action.startswith('smalltalk'):
            bot_responses = f'{bot_response}<br><br>{bot_responses}'
        else:
            bot_responses += f'{bot_response}<br>'
        bot_responses = str(bot_responses)
        return bot_responses
