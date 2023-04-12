import pandas as pd
import numpy as np
from scipy.stats import kruskal

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(x,y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p = kruskal(x,y).pvalue
    return p<0.05
