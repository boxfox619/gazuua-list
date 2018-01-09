import pickle
from recommender import crypto_recommender
from price_api import get_newone

with open('./pkl/history.pkl', 'rb') as f:
    history = pickle.load(f)
    new = get_newone()
    recommend = crypto_recommender(history, new, n_recommend = 10)
    print(recommend)
