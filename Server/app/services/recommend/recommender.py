
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import  NearestNeighbors

def scoring(history, newone, k = 600):
    model = NearestNeighbors(n_neighbors = k, metric = 'cosine', n_jobs = -1)
    model.fit(history['history'])

    distances, neigbors = model.kneighbors(newone, return_distance = True)

    pred = np.zeros(newone.shape[0])
    for i in range(newone.shape[0]):
        pred[i] = history['target'][neigbors[i]].dot(distances[i]) / np.abs(distances[i]).sum()

    return pred

def crypto_recommender(history, names, values, n_recommend = 5):
    score = scoring(history, values, k = 600)
    coin_lst = sorted([(n, v) for (n, v) in zip(names, score)], key = lambda x: x[1], reverse = True)
    recommend = coin_lst[:n_recommend]
    return recommend


