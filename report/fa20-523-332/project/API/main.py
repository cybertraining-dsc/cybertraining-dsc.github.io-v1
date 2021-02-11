from flask import Flask, jsonify
from db_utils import *
import datetime as dt

app = Flask(__name__)

@app.route('/')
def home():
    result = { 
        "status" : "Success", 
        "details" : "This is a prototype API for an academic project.",
        "developer" : "Krish Hemant Mhatre",
        "topic" : "Analyzing the Relationship of Cryptocurrencies with Foriegn Exchange Rates and Global Stock Market Indices"
        }
    return jsonify(result)

@app.route('/get_data/single/<market>/<index>/<date>', methods=['GET'])
def get_data(market, index, date):
    result = {}
    try:
        tmp = dt.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        result['status'] = 'Error'
        result['data'] = 'Incorrect Date Format'
        return result
    data = single_data(market, index, date)
    if len(data) > 0:
        result['status'] = 'Success'
        result['data'] = data
    else:
        result['status'] = 'Error'
        result['data'] = 'No Data Found'
    return jsonify(result)

@app.route('/get_data/multiple/<market>/<index>/<start_date>/<end_date>', methods=['GET'])
def get_multiple_data(market, index, start_date, end_date):
    result = {}
    try:
        tmp = dt.datetime.strptime(start_date, "%Y-%m-%d")
        tmp = dt.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        result['status'] = 'Error'
        result['data'] = 'Incorrect Date Format'
        return result
    if int(str(dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.datetime.strptime(start_date, '%Y-%m-%d')).split(' ')[0]) < 1:
        result['status'] = 'Error'
        result['data'] = 'Incorrect Date Values'
    else:
        data = range_data(market, index, start_date, end_date)
        if len(data) > 0:
            result['status'] = 'Success'
            result['data'] = data
        else:
            result['status'] = 'Error'
            result['data'] = 'No Data Found'
    return jsonify(result)

@app.route('/get_predictions/<date>', methods=['GET'])
def get_predictions(date):
    result = {}
    try:
        tmp = dt.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        result['status'] = 'Error'
        result['data'] = 'Incorrect Date Format'
        return result
    data = predictions(date)
    if len(data) > 0:
        result['status'] = 'Success'
        result['data'] = data
    else:
        result['status'] = 'Error'
        result['data'] = 'No Data Found'
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)