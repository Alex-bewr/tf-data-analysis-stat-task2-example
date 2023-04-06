import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 441809625 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы

    b_hat = np.max(x)
    n = len(x)

    eps1 = (1 - p) / 100;
    left = b_hat/np.power(p+eps1, 1/n)
    right = b_hat/np.power(eps1, 1/n)

    lengh = right - left

    for k in np.arange(eps1, 1-p-eps1, 0.0001):
        eps = k;

        left_new = b_hat/np.power(p+k, 1/n)
        right_new = b_hat/np.power(k, 1/n)
        lengh_new = right_new - left_new

        if (lengh_new < lengh):
          left = left_new
          right = right_new
          lengh = lengh_new
    

    return [left, right];
