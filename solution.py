import pandas as pd
import numpy as np


chat_id = 5437824033 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t=10
    n = len(x)
    mu = 7
    for i in range(n):
        x[i] = (x[i] + 7) / t 
    return x.mean() # Ваш ответ
