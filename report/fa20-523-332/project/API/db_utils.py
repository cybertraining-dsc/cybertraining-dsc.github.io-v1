import pymongo
import datetime as dt
import os

PASSWORD = os.environ['PASSWORD']

def get_db_path(database):
    db_path = "mongodb+srv://kmhatre:" + PASSWORD + "@crypto.j5hw0.mongodb.net/" + database + "?retryWrites=true&w=majority"
    return db_path

def datelist(start_date, end_date):
  days = int((dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.datetime.strptime(start_date, '%Y-%m-%d')).days)
  date_list = [str(dt.datetime.strptime(end_date, '%Y-%m-%d') - dt.timedelta(days=x))[:10] for x in range(days+1)]
  return date_list

def single_data(database, collection, date):
    client = pymongo.MongoClient(get_db_path(database))
    db = client[database]
    col = db[collection]
    query = { "formatted_date": date }
    doc = col.find(query)
    result = []
    for x in doc:
        result.append( { 'high' : x['high'], 'low' : x['low'], 'open' : x['open'], 'close' : x['close'], 'date' : x['formatted_date']} )
    return result

def range_data(database, collection, start_date, end_date):
    client = pymongo.MongoClient(get_db_path(database))
    db = client[database]
    col = db[collection]
    dates = datelist(start_date, end_date)
    result = []
    for x in col.find():
        if x['formatted_date'] in dates:
            result.append( { 'high' : x['high'], 'low' : x['low'], 'open' : x['open'], 'close' : x['close'], 'date' : x['formatted_date']} )
    return result

def predictions(date):
    client = pymongo.MongoClient(get_db_path('predictions'))
    db = client['predictions']
    col = db['predictions']
    query = { 'date' : date }
    doc = col.find(query)
    result = []
    for x in doc:
        result.append( { 
            'date' : x['date'], 
            'bitcoin': x['bitcoin_pred'], 
            'dash': x['dash_pred'], 
            'ethereum': x['ethereum_pred'],  
            'litecoin': x['litecoin_pred'], 
            'monero': x['monero_pred'], 
            'ripple': x['ripple_pred'] 
            })
    return result
    