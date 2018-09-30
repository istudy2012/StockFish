import json

import requests

from datasource.Juhe import *


def fetch_today_info(stock_code):
    real_stock_code = get_real_stock(stock_code)
    params = {
        "key": stock_app_key,
        "gid": real_stock_code,
    }

    url = stock_detail_url
    response = requests.get(url, params)
    return parse_content(response.content)


def parse_content(content):
    json_dict = json.loads(content)
    if json_dict['reason'] != 'SUCCESSED!':
        print('error request:' + content)
        return []
    else:
        return json_dict['result'][0]['data']


def get_real_stock(stock_code):
    c = stock_code[0]
    if is_sh_stock(stock_code):
        return 'sh' + stock_code
    elif is_sz_stock(stock_code):
        return 'sz' + stock_code
    else:
        return stock_code


def is_sh_stock(stock_code):
    return stock_code[0:2] == '60'


def is_sz_stock(stock_code):
    return stock_code[0:2] == '00' or stock_code[0:3] == '300'
