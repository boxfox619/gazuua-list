import pickle
import sys
import datetime
import multiprocessing
import time

from .recommender import crypto_recommender
from .price_api import get_newone, get_all_ticker
from time import sleep
from apscheduler.scheduler import Scheduler

from app.models.coin import CoinModel, RecommendModel

sched = Scheduler()
sched.start()

prevTime = 19990619

def updateRecommends():
    print('update recommend coins')
    with open('app/services/recommend/pkl/history.pkl', 'rb') as f:
        RecommendModel.objects().delete()
        history = pickle.load(f)
        new = get_newone()
        recommend = crypto_recommender(history, new, n_recommend = 5)
        for item in recommend:
            RecommendModel(symbol=item[0], score=item[1]).save()

def updateCoins():
    print('update coin price')
    tickers = get_all_ticker()
    CoinModel.objects().delete()
    for ticker in tickers:
        CoinModel(
        symbol=ticker[0],
        name=ticker[1],
        rate=ticker[2]).save()

def update():
    while True:
        updateCoins()
        date = datetime.datetime.now()
        now = date.year + date.month + date.day
        if prevTime != now:
            updateRecommends()
        time.sleep(15)

def init():
    multiprocessing.Process(target=update).start()
