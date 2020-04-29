import requests
import os
from dotenv import load_dotenv
import logging
import datetime
import plotly.graph_objects as go

VERSION_VKONTAKTE = '5.52'
PERIOD_OF_DAYS_ANALYSIS = 7

def get_url(api_method):
    url = f'https://api.vk.com/method/{api_method}'
    return url

def get_data_from_site(url, params, headers=None):
    response = requests.get(url, headers=headers or {}, params=params)
    response.raise_for_status()
    return response.json()

def get_table_of_periods():
    list_of_periods = []
    today = datetime.datetime.now()

    for number_of_days in range(PERIOD_OF_DAYS_ANALYSIS):
        day = today - datetime.timedelta(days=number_of_days)
        daystamp = day.timestamp()
        list_of_periods.append((day, daystamp))

    return list_of_periods

def get_occurrences():
    occurrences = [[],[]]
    vk_service_key = os.getenv('VK_SERVICE_KEY')
    params = {'v':VERSION_VKONTAKTE,'access_token':vk_service_key}
    params['q'] = 'Coca-Cola'

    list_of_periods = get_table_of_periods()
    url = get_url('newsfeed.search')

    for i, period in enumerate(list_of_periods[1:]):
        num_of_posts = 0
        end_time = list_of_periods[i][0]
        params['start_time'] = period[1]
        params['end_time'] = list_of_periods[i][1]
        data_from_site = get_data_from_site(url, params)
        if data_from_site:
            num_of_posts = data_from_site['response'].get('total_count',0)
            
        occurrences[0].append(end_time.strftime('%d.%m.%Y'))
        occurrences[1].append(num_of_posts)
        
    return occurrences
    
def main():
    
    load_dotenv()
    logging.basicConfig(level = logging.DEBUG, filename = u'log.txt')
    occurrences = None
    try:
        occurrences = get_occurrences()
    except requests.exceptions.HTTPError as error:
        logging.error('Не удалось получить данные с сайта vk.com: {0}'.format(error))
    except requests.exceptions.ConnectionError as error:
        logging.error('Не удалось получить данные с сайта vk.com: {0}'.format(error))
    except (KeyError, TypeError) as error:
        logging.error('Ошибка анализа данных с сайта vk.com: {0}'.format(error))

    if occurrences:  
        fig = go.Figure([go.Bar(x=occurrences[0][::-1], y=occurrences[1][::-1])])
        fig.show()

if __name__=='__main__':
    main()