from numpy import random, mean, var, std

n = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
xm = mean(n)  # среднеарифметическое
xv = var(n, ddof=1)  # дисперсия(n - 1)
m = std(n)  # среднеквадратическое отклонение
