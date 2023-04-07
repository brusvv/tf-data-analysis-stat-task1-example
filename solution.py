import pandas as pd
import numpy as np


chat_id = 5437824033 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    sample_mean = np.mean(x)
    sample_var = np.var(x, ddof=1)
    t = exp(1)
    delta = t * np.sqrt(sample_var / n)
    acceleration = 2 * (np.log(sample_mean + delta) - np.log(10)) / 10
    return acceleration.mean()
