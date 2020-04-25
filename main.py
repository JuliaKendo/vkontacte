import requests
import os
from dotenv import load_dotenv
import logging
import time
import datetime
import plotly.graph_objects as go

load_dotenv()
logging.basicConfig(level = logging.DEBUG, filename = u'log.txt')

VERSION_VKONTACTE = '5.52'
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
PERIOD_OF_DAYS_ANALYSIS = 7

def get_url(url_method, params=None):
    url = f'https://api.vk.com/method/{url_method}'
    return url

def query_to_site(Url, Params, Headers=None):
    try:
        if Headers:
            responce = requests.get(Url, headers=Headers, params=Params)
        else:
            responce = requests.get(Url, params=Params)
    except requests.exceptions.HTTPError as error:
        logging.error(u'Ошибка получения данных по ссылке {0}:\n{1}'.format(Url, error))
        return {}
    responce.raise_for_status()
    return responce.json()

def get_table_of_periods():
    list_of_periods = []
    today = datetime.datetime.now()

    for number_of_days in range(PERIOD_OF_DAYS_ANALYSIS):
        day = today - datetime.timedelta(days=number_of_days)
        daystamp = day.timestamp()
        list_of_periods.append((day, daystamp))

    return list_of_periods

def get_occurence():
    occurence = [[],[]]
    params = {'v':VERSION_VKONTACTE,'access_token':ACCESS_TOKEN}
    params['q'] = 'Coca-Cola'

    list_of_periods = get_table_of_periods()
    url = get_url('newsfeed.search')

    for i, period in enumerate(list_of_periods[1:]):
        num_of_posts = 0
        end_time = list_of_periods[i][0]
        params['start_time'] = period[1]
        params['end_time'] = list_of_periods[i][1]
        while True:
            json_info = query_to_site(url, params)
            time.sleep(1)
            next_form = json_info['response'].get('next_from')
            if not next_form:
                break
            for item in json_info['response']['items']:
                num_of_posts += 1

            params['start_from'] = next_form
        occurence[0].append(end_time.strftime('%d.%m.%Y'))
        occurence[1].append(num_of_posts)

    return occurence
    
def main():
    occurence = get_occurence() 
    if len(occurence) > 0:  
        fig = go.Figure([go.Bar(x=occurence[0][::-1], y=occurence[1][::-1])])
        fig.show()

if __name__=='__main__':
    main()