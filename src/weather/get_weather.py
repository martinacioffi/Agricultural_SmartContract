#!/usr/bin/env python
# coding: utf-8

import logging
import configparser
from pandas.io.json import json_normalize
from geopy.geocoders import Nominatim
from dateutil.relativedelta import relativedelta
from datetime import date
import requests
import pandas as pd


logger = logging.getLogger('weather_logging')
hdlr = logging.FileHandler('weather_logging.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['meteostat']['api']


def weather(where: str, start: str, end: str, time_range: str = 'monthly', distlimit: int = 5):

    api = '2arOOWuC'  # get_api_key()
    geolocator = Nominatim(user_agent='weather-app')
    loc = geolocator.geocode(where)

    try:
        link_loc = (f'https://api.meteostat.net/v1/stations/nearby?'
                    f'lat={loc.latitude}&lon={loc.longitude}&limit={distlimit}&key={api}')
        req = requests.get(link_loc).json()['data']

        try:
            i = 0
            while i < 3:

                station_id = req[i]['id']
                distance = req[i]['distance']
                station_name = req[i]['name']
                print(f'Closest station and relative distance: {station_name}, {distance}')

                link_data = (f'https://api.meteostat.net/v1/history/{time_range}?'
                             f'station={station_id}&start={start}&end={end}&key={api}')

                output = json_normalize(requests.get(link_data).json()['data'])

                if not output.empty:
                    break
                i += 1

            logger.info(f'Task finished with station {where} and index {i}')
            return i, output, distance

        except BaseException as e:
            logger.error(f'No station near {where} with available data -- {str(e)}')
            raise e

    except BaseException as e:
        logger.error(f'No location like {where} -- {str(e)}')
        raise e


def weather_df(where: str, start: str, end: str, time_range: str = 'monthly', distlimit: int = 5) -> pd.DataFrame:
    df = weather(where, start, end, time_range, distlimit)[1][['date', 'precipitation']]
    df['date'] = pd.to_datetime(df['month'])
    df['date'] = df['month'].dt.strftime('%m/%Y')
    return df


def avg_precipitation(where: str, month: int, year_range: str = '10'):
    month = int(month)
    assert (1 <= month <= 12)

    end = date.today().replace(day=1, month=month) + relativedelta(months=+1) + relativedelta(days=-1)

    if year_range == 'max':
        start = end.replace(year=end.year - 49, day=1)
    else:
        start = end.replace(year=end.year - int(year_range) + 1, day=1)

    precip = weather(where, start.strftime('%Y/%m/%d'), end.strftime('%Y/%m/%d'),
                     time_range='daily')[1]

    precip.date = pd.to_datetime(precip.date)
    mask = precip.date.map(lambda x: x.month) == month
    precip = precip[mask].precipitation
    return precip
