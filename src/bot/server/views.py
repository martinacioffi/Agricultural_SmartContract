from flask import render_template, redirect, url_for, request, Blueprint
from src.bot.create_chatbot.helpers import detect_intent_texts
from src.contract import create_contract

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
        #TODO get the right parameters from the json session vars
        _, __, ___, _____, utterance = create_contract('milan', 4, 32, 'johndoe.eth')
        return utterance
    else:
        bot_responses = ''
        action, bot_response, params = detect_intent_texts('agrisc-tafasq', session, raw_query)
        if action.startswith('smalltalk'):
            bot_responses = f'{bot_response}<br><br>{bot_responses}'
        else:
            bot_responses += f'{bot_response}<br>'
        bot_responses = str(bot_responses)
        return bot_responses
