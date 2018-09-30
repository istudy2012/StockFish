from stockcode import StockCodeDatabase
from stockinfo import StockInfoFetcher


def main():
    with open('stock.txt') as fp:
        items = fp.readlines()

        stocks = []
        for item in items:
            if len(item.strip()) > 0:
                stocks.append(item.replace('\n', ''))

    if len(stocks) == 0:
        print("Empty stock")
        return

    result = StockCodeDatabase.query(stocks)
    print('All stock: ' + result.__str__())
    print('All stock size: {0}'.format(len(result)))

    response = []
    print('Fetching...')
    for i in result:
        code = i[1]
        response.append(StockInfoFetcher.fetch_today_info(code))

    print("Calculating...")
    inc_sum = 0.0
    for i in response:
        print('{0} : {1}'.format(i['name'], i['increPer']))
        inc_sum += float(i['increPer'])
    print('Total average: {0}'.format(inc_sum / response.__len__()))


if __name__ == '__main__':
    main()
