import requests
import json
import datetime


def get_feriados():
    day = datetime.date.today().day
    month = datetime.date.today().month
    year = datetime.date.today().year
    res = requests.get('https://brasilapi.com.br/api/feriados/v1/{}'.format(str(year)))
    for item in json.loads(res.text):
        date = item['date'].split('-')
        print(date)
                
    
get_feriados()