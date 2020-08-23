import requests
import pandas

response = requests.get('https://crix-api-cdn.upbit.com/v1/crix/candles/days?code=CRIX.UPBIT.KRW-BTC&count=200&ciqrandom=1568240649168')

result = {
    'code' : [],
    'candleDateTime' : [],
    'candleDateTimeKst' : [],
    'openingPrice' : [],
    'highPrice' : [],
    'lowPrice' : [],
    'tradePrice' : [],
    'candleAccTradeVolume' : [],
    'candleAccTradePrice' : [],
    'timestamp' : [],
    'prevClosingPrice' : [],
    'change' : [],
    'changePrice' : [],
    'signedChangePrice' : [],
    'changeRate' : [],
    'signedChangeRate' : [],
}

for item in response.json() :
    result['code'].append(item['code'])
    result['candleDateTime'].append(item['candleDateTime'])
    result['candleDateTimeKst'].append(item['candleDateTimeKst'])
    result['openingPrice'].append(item['openingPrice'])
    result['highPrice'].append(item['highPrice'])
    result['lowPrice'].append(item['lowPrice'])
    result['tradePrice'].append(item['tradePrice'])
    result['candleAccTradeVolume'].append(item['candleAccTradeVolume'])
    result['candleAccTradePrice'].append(item['candleAccTradePrice'])
    result['timestamp'].append(item['timestamp'])
    result['prevClosingPrice'].append(item['prevClosingPrice'])
    result['change'].append(item['change'])
    result['changePrice'].append(item['changePrice'])
    result['signedChangePrice'].append(item['signedChangePrice'])
    result['changeRate'].append(item['changeRate'])
    result['signedChangeRate'].append(item['signedChangeRate'])

df = pandas.DataFrame(result)
print(df)

df.to_csv('upbit.csv') # csv저장