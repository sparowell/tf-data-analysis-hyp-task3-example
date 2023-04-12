import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(x,y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    #p = kruskal(x,y).pvalue
    p = ks_2samp(x,y,alternative='lower').pvalue
    return p<0.05
