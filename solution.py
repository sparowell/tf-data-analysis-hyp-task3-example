import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(x,y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    #p = kruskal(x,y).pvalue
    #p = ks_2samp(x,y,alternative='lower').pvalue
    p = MMD(compute_kernel="rbf", gamma=10).test(x, y)[1]
    return p<0.05
