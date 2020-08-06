from scipy import stats as st
from scipy.stats import chisquare


F = 2.5
m = 3  # количество групп
N = 10 * m  # размер общей выборки
dfw = N - m  # внутригрупповое число степеней свободы
dfb = m - 1  # межгрупповое число степеней свободы
p = 1 - st.f.cdf(F, dfb, dfw)
print('Принимаем' if p > 0.05 else 'Отклонить')


b = chisquare([18, 55, 27], f_exp=[25, 50, 25])
# расчет хи квадрата
