import numpy as np
import math

random_numbers = np.random.uniform(-np.pi/2, np.pi/2, 10000)
errors_sin_t_6 = []
errors_cos_t_6 = []
errors_sin_t_7 = []
errors_cos_t_7 = []

for number in random_numbers:
    t_6 = (10395*number - 1260*number**3 + 21*number**5) / (10395 - 4725*number**2 + 210*number**4 - number**6)
    t_7 = (135135*number - 17325*number**3 + 378*number**5 - number**7) / (135135 - 62370*number**2 + 3150*number**4 - 28*number**6)
    sin_t_6 = t_6 / math.sqrt(1 + t_6**2)
    cos_t_6 = 1 / math.sqrt(1 + t_6**2)
    sin_t_7 = t_7 / math.sqrt(1 + t_7**2)
    cos_t_7 = 1 / math.sqrt(1 + t_7**2)

    tangenta = math.tan(number)
    sinus = tangenta / math.sqrt(1 + tangenta**2)
    cosinus = 1 / math.sqrt(1 + tangenta**2)

    # sin_val = math.sin(number) = sinus
    # cos_val = math.cos(number) = cosinus

    errors = [abs(sin_t_6 - sinus), abs(cos_t_6 - cosinus), abs(sin_t_7 - sinus), abs(cos_t_7 - cosinus)]

    errors_sin_t_6.append(errors[0])
    errors_cos_t_6.append(errors[1])
    errors_sin_t_7.append(errors[2])
    errors_cos_t_7.append(errors[3])

avg_erros = {'sin_t_6': sum(errors_sin_t_6) / len(errors_sin_t_6), 'cos_t_6': sum(errors_cos_t_6) / len(errors_cos_t_6), 'sin_t_7': sum(errors_sin_t_7) / len(errors_sin_t_7), 'cos_t_7': sum(errors_cos_t_7) / len(errors_cos_t_7)}
sorted_avg_errors = sorted(avg_erros.items(), key=lambda x: x[1])

print('The best approximation is:', sorted_avg_errors[0][0], 'with the average error:', sorted_avg_errors[0][1])
print('The worst approximation is:', sorted_avg_errors[-1][0], 'with the average error:', sorted_avg_errors[-1][1])




