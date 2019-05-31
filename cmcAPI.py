from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os, threading


with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


parameters = {
    'start':'1',
    'limit':'200',
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.environ.get('APIkey')
}


session = Session()
session.headers.update(headers)


def get_data():
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    return data
