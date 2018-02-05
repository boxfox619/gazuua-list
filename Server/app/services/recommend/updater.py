import pickle
import sys
import datetime
import time
import multiprocessing

from app.models import Mongo
from .recommender import crypto_recommender
from .price_api import get_newone, get_all_ticker
from time import sleep
from apscheduler.scheduler import Scheduler

from app.models.coin import CoinModel, RecommendModel


db = Mongo()
# To Control MongoDB

sched = Scheduler()
sched.start()


def updateRecommends():
    print('update recommend coins')
    with open('app/services/recommend/pkl/history.pkl', 'rb') as f:
        RecommendModel.objects().delete()
        history = pickle.load(f)
        names, values = get_newone()
        recommend = crypto_recommender(history, names, values, n_recommend = 5)
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

def update(app_):
    print('init')
    global prev_time
    prev_time = 19990619
    db.init_app(app_)
    while True:
        updateCoins()
        date = datetime.datetime.now()
        now = date.year + date.month + date.day
        if prev_time != now:
            updateRecommends()
            prev_time = now

def init(app_):
    p = multiprocessing.Process(target=update, args=[app_,])
    p.start()
    multiprocessing.Process(target=update, args=(app_,)).start()
