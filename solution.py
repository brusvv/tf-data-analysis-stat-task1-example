import pandas as pd
import numpy as np


chat_id = 5437824033 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    total_lamps = np.sum(x)
    lambda_ = total_lamps / (len(x) * 39)
    return lambda_ # Ваш ответ
