import pickle
import sys
import datetime

from .recommender import crypto_recommender
from .price_api import get_newone, get_all_ticker
from time import sleep
from apscheduler.scheduler import Scheduler

from app.models.coin import CoinModel, RecommendModel

sched = Scheduler()
sched.start()


def updateRecommends():
    print('update recommend coins')
    with open('app/services/recommend/pkl/history.pkl', 'rb') as f:
        RecommendModel.objects().delete()
        history = pickle.load(f)
        new = get_newone()
        recommend = crypto_recommender(history, new, n_recommend = 5)
        for item in recommend:
            RecommendModel(symbol=item[0], score=item[1]).save()

    scheduleDate = getScheduleDate()
    sched.add_date_job(updateRecommends, scheduleDate, [])

def getScheduleDate():
    now = datetime.datetime.now()
    str_list = [now.year, '-', now.month, '-', now.day+1, ' 00:00:00']
    return ''.join(str(v) for v in str_list)

def updateCoins():
    print('update coin price')
    tickers = get_all_ticker()
    CoinModel.objects().delete()
    for ticker in tickers:
        CoinModel(
        symbol=ticker[0],
        name=ticker[1],
        rate=ticker[2]).save()
    sched.add_interval_job(updateCoins, seconds=15, args=[])


def start():
    updateRecommends()
    updateCoins()
