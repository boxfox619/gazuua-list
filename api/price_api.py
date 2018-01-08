
# coding: utf-8

import pandas as pd
import numpy as np
import requests as rq
import datetime
import time

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
    
    today = datetime.datetime.now().date()
    start = today - datetime.timedelta(8)
    end = today - datetime.timedelta(1)
    start = int(time.mktime(datetime.datetime(start.year, start.month, start.day, 0).timetuple()))
    end = int(time.mktime(datetime.datetime(end.year, end.month, end.day, 23).timetuple()))
    
    newone = []
    for coin_cd in coin.keys():
        res = get_json(coin_cd, start, end)
        price = []

        for tick in res.json():
            if datetime.datetime.fromtimestamp(tick['date']).minute == 0:
                price.append(tick['close'])

        newone.append((coin_cd, price))
    newone = pd.DataFrame(newone, columns = ['name', 'ts']).set_index('name')
    
    return(newone)


