
# coding: utf-8

# In[167]:

import pandas as pd
import numpy as np

def find_code(data, target, k):     
    corr = []
    idx_lst = data.index
    for idx in idx_lst:
        value = np.corrcoef(x = target, y = data.loc[idx, 'ts'])[0, 1]
        corr.append(value)
    
    corr = pd.Series(corr, index = idx_lst).sort_values(ascending = False)
    top = list(corr.index[:k])
    value = np.mean(corr.loc[top])
    
    return(top, value)

def scoring(data, target, k):
    score = 0
    top, value = find_code(data, target, k)
    candi = data.loc[top, ['target1', 'target3', 'target7']].mean(axis = 0)
    score += candi['target1'] * 10
    score += candi['target3'] * 5
    score += candi['target7'] * 1
    score /= (10 + 5 + 3 + 1)
    
    return(score)


# ### 67개 암호화폐 스코어 계산: 2분 24초

# In[233]:

def cryto_recommender(history, new, n_recommend = 5):
    result = []
    for i in new.index:
        target = new.loc[i, 'ts']
        result.append((i, scoring(data = history, target = target, k = 55)))

    recommend = sorted(result, key = lambda x: x[1], reverse = True)[:n_recommend]
    return(recommend)


