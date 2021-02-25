from nomics import Nomics
APIkey = '720b0eebbf4d02ee210818ba2e685239'
nomics = Nomics(key)
print(nomics.ExchangeRates.get_rates())

'''
markets = nomics.Markets.get_markets(exchange = 'binance')
btc_markets = [market for market in markets if market['quote'] == 'BTC']
'''
