
# coding: utf-8

import pandas as pd
import numpy as np
import requests as rq
import datetime
import time

coin = {'XRP': 'Ripple',
            'STR': 'Stella',
            'ETH': 'ethereum',
            'XEM': 'NEM',
            'DGB': 'DigiBite',
            'SC': 'Siacoin',
            'LTC': 'Litecoin',
            'ETC': 'Ethereum Classic',
            'BCH': 'Bitcoin Cash',
            'DOGE': 'Dogecoin',
            'DASH': 'Dash',
            'BTS': 'BitShares',
            'XMR': 'Monero',
            'NXT': 'NXT',
            'LSK': 'Lisk',
            'STEEM': 'STEEM',
            'BCN': 'Bytecoin',
            'FCT': 'Factom',
            'STRAT': 'Stratis',
            'BURST': 'Burst',
            'ZEC': 'Zcash',
            'OMG': 'OmiseGO',
            'EMC2': 'Einsteinium',
            'ARDR': 'Ardor',
            'REP': 'Augur',
            'ZRX': '0x',
            'GNT': 'Golem',
            'CVC': 'Civic',
            'LBC': 'LBRY Credits',
            'MAID': 'MaidSafeCoin',
            'GAME': 'GameCredits',
            'VTC': 'Vertcoin',
            'SYS': 'Syscoin',
            'DCR': 'Decred',
            'STORJ': 'Storj',
            'XCP': 'Counterparty',
            'AMP': 'Synereo AMP',
            'PASC': 'PascalCoin',
            'GAS': 'Gas',
            'GNO': 'Gnosis',
            'FLDC': 'FoldingCoin',
            'POT': 'PotCoin',
            'NXC': 'Nexium',
            'NAV': 'NAVCoin',
            'BELA': 'Bela',
            'VRC': 'VeriCoin',
            'OMNI': 'Omni',
            'CLAM': 'CLAMS',
            'GRC': 'Gridcoin Research',
            'NEOS': 'Neoscoin',
            'EXP': 'Expanse',
            'VIA': 'Viacoin',
            'BLK': 'BlackCoin',
            'XVC': 'Vcash',
            'PINK': 'Pinkcoin',
            'NMC': 'Namecoin',
            'RADS': 'Radium',
            'XPM': 'Primecoin',
            'SBD': 'Steem Dollars',
            'XBC': 'BitcoinPlus',
            'BCY': 'BitCrystals',
            'RIC': 'Riecoin',
            'PPC': 'Peercoin',
            'BTM': 'Bitmark',
            'FLO': 'Florincoin',
            'HUC': 'Huntercoin',
            'BTCD': 'BitcoinDark'}

# In[3]:

def get_json(coin_cd, start, end):
    url = 'https://poloniex.com/public'

    res = rq.get(url, params = {'command': 'returnChartData',
                                'currencyPair': 'BTC_%s' % coin_cd,
                                'start': start,
                                'end': end,
                                'period': 1800})
    
    return(res)

def get_history(res, coin_cd):
    history = []
    for tick in res.json():
        date = datetime.datetime.fromtimestamp(tick['date']).strftime('%Y-%m-%d')
        hour = datetime.datetime.fromtimestamp(tick['date']).hour
        minute = datetime.datetime.fromtimestamp(tick['date']).minute
        price = tick['close']

        value = (date, hour, minute, price)
        history.append(value)

    dfm = pd.DataFrame(history, columns = ['date', 'hour', 'minute', 'price'])
    dfm.to_csv('./data/%s.csv' % (coin_cd), index = False)


# In[ ]:

def get_newone():
    import pandas as pd
    import numpy as np
    import requests as rq
    import datetime
    import time
    
    today = datetime.datetime.now()
    start = today - datetime.timedelta(8)
    end = today - datetime.timedelta(1)
    start = int(time.mktime(datetime.datetime(start.year, start.month, start.day, start.hour - 1).timetuple()))
    end = int(time.mktime(datetime.datetime(end.year, end.month, end.day, end.hour).timetuple()))

    values = np.zeros((len(coin), 168))
    names = list(coin.keys())   
    for i in range(len(names)):
        coin_cd = names[i]
        res = get_json(coin_cd, start, end)
        price = []

        for tick in res.json():
            if datetime.datetime.fromtimestamp(tick['date']).minute == 0:
                price.append(tick['close'])

        price = pd.Series(price).iloc[-169:]
        price = np.array(price.pct_change()[1:].values)
        values[i, :] = price
    
    return(names, values)

def get_ticker(symbol, take = 'percentChange'):
    url = 'https://poloniex.com/public?command=returnTicker'
    res = rq.get(url)
    ticker = res.json()
    information = float(ticker['BTC_' + symbol][take])
    
    return(information)

def get_all_ticker():
    tickers = []
    for coin_cd in coin.keys():
        tickers.append([coin_cd, coin[coin_cd], get_ticker(coin_cd)])

    return (tickers)


