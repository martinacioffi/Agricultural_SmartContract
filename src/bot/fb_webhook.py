from flask import Flask, request, make_response, jsonify
from src.weather.get_weather import avg_precipitation
from src.contract import create_contract, create_new_address

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


def results():
    req = request.get_json(force=True)
    print(req)
    action = req.get('queryResult').get('action')
    if action == 'ConfirmProceed':
        res = contract_response(req)
        return {'fulfillmentText': res}


def contract_response(req):
    ctxs = req.get('queryResult').get('outputContexts')
    d = next(item for item in ctxs if item['name'].endswith('session_vars'))
    location = d['parameters']['geo-city']
    month = d['parameters']['date-period']['startDate'].split('-')[1].replace('0', '')
    precipitation = avg_precipitation(location, month)
    address = create_new_address()
    _, __, ___, _____, result = create_contract(location, int(month), precipitation, address)
    return result


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))


if __name__ == '__main__':
    app.run(port=8000, debug=True)
