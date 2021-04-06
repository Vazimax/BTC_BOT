import requests
import time 
import os


api_key =  os.environ.get('API_KEY')
bot_key =  os.environ.get('BOT_KEY')
chat_id =  os.environ.get('CHAT_ID')
limit = 60000
time_interval = 3


def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start' : '1',
        'limit' : '2',
    }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url,headers=headers,params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price

def send_message(chat_id,msg):
    url = f'https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}'

    requests.get(url)

def main_fun():
    while True:
        price = get_price()
        if price < limit:
            send_message(chat_id,f"The btc price is : {price}")
        time.sleep(time_interval)

main_fun()