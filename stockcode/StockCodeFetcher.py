import json

import requests

from datasource import Juhe
from helper import HttpHelper
from stockcode import StockCodeDatabase


def refresh():
    StockCodeDatabase.create()

    refresh_sh()
    refresh_sz()


def refresh_sh():
    url = Juhe.stock_sh_list_url
    download(url, 0)


def refresh_sz():
    url = Juhe.stock_sz_list_url
    download(url, 0)


def download(url, page=0):
    params = {
        'key': Juhe.stock_app_key,
        'page': page,
        'type': 4
    }
    response = requests.get(url, params)
    print("fetching url: " + response.url)
    if HttpHelper.is_success(response.status_code):
        json_data = json.loads(response.content)
        if json_data['error_code'] == 0:
            if len(json_data['result']['data']) != 0:
                print("saving url: " + response.url)
                save_data(json_data['result']['data'])
                download(url, page + 1)
            else:
                return
        else:
            print("fetch finish url: " + response.url)
            return
    else:
        print(
            "fetch api failure url : " + response.url + " , status_code :" + response.status_code + ", errorContent: " + response.content)


def save_data(data):
    items = []
    for info in data:
        item = [info['name'], info['symbol']]
        items.append(item)

    StockCodeDatabase.insert(items)
