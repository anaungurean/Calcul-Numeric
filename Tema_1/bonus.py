import numpy as np
import math

random_numbers = np.random.uniform(-np.pi/2, np.pi/2, 10000)
errors_sin_t_4 = []
errors_cos_t_4 = []
errors_sin_t_5 = []
errors_cos_t_5 = []
errors_sin_t_6 = []
errors_cos_t_6 = []
errors_sin_t_7 = []
errors_cos_t_7 = []
errors_sin_t_8 = []
errors_cos_t_8 = []
errors_sin_t_9 = []
errors_cos_t_9 = []

for number in random_numbers:
    t_4 = (105*number - 10*number**3) / (105 - 45*number**2 + number**4)
    t_5 = (945*number - 105*number**3 + number**5) / (945 - 420*number**2 + 15*number**4)
    t_6 = (10395*number - 1260*number**3 + 21*number**5) / (10395 - 4725*number**2 + 210*number**4 - number**6)
    t_7 = (135135*number - 17325*number**3 + 378*number**5 - number**7) / (135135 - 62370*number**2 + 3150*number**4 - 28*number**6)
    t_8 = (2027025*number - 270270*number**3 + 6930*number**5 - 36*number**7) / (2027025 - 945945*number**2 + 51975*number**4 - 630*number**6 + number**8)
    t_9 = (34459425*number - 4729725*number**3 + 135135*number**5 - 990*number**7 + number**9) / (34459425 - 16216200*number**2 + 945945*number**4 - 13860*number**6 + 45*number**8)
    sin_t_4 = t_4 / math.sqrt(1 + t_4 ** 2)
    cos_t_4 = 1 / math.sqrt(1 + t_4 ** 2)

    sin_t_5 = t_5 / math.sqrt(1 + t_5 ** 2)
    cos_t_5 = 1 / math.sqrt(1 + t_5 ** 2)

    sin_t_6 = t_6 / math.sqrt(1 + t_6**2)
    cos_t_6 = 1 / math.sqrt(1 + t_6**2)

    sin_t_7 = t_7 / math.sqrt(1 + t_7**2)
    cos_t_7 = 1 / math.sqrt(1 + t_7**2)

    sin_t_8 = t_8 / math.sqrt(1 + t_8**2)
    cos_t_8 = 1 / math.sqrt(1 + t_8**2)

    sin_t_9 = t_9 / math.sqrt(1 + t_9**2)
    cos_t_9 = 1 / math.sqrt(1 + t_9**2)

    tangenta = math.tan(number)
    sinus = tangenta / math.sqrt(1 + tangenta**2)
    cosinus = 1 / math.sqrt(1 + tangenta**2)

    errors_sin = [abs(sin_t_4 - sinus), abs(sin_t_5 - sinus), abs(sin_t_6 - sinus), abs(sin_t_7 - sinus), abs(sin_t_8 - sinus), abs(sin_t_9 - sinus)]
    errors_cos = [abs(cos_t_4 - cosinus), abs(cos_t_5 - cosinus), abs(cos_t_6 - cosinus), abs(cos_t_7 - cosinus), abs(cos_t_8 - cosinus), abs(cos_t_9 - cosinus)]
    print('For number:', number, 'the best approximation for sinus is:', errors_sin.index(min(errors_sin)) + 4, 'with the error:', min(errors_sin))
    print('For number:', number, 'the best approximation for cosinus is:', errors_cos.index(min(errors_cos)) + 4, 'with the error:', min(errors_cos))

    # sin_val = math.sin(number) = sinus
    # cos_val = math.cos(number) = cosinus

    errors_sin_t_4.append(errors_sin[0])
    errors_cos_t_4.append(errors_cos[0])
    errors_sin_t_5.append(errors_sin[1])
    errors_cos_t_5.append(errors_cos[1])
    errors_sin_t_6.append(errors_sin[2])
    errors_cos_t_6.append(errors_cos[2])
    errors_sin_t_7.append(errors_sin[3])
    errors_cos_t_7.append(errors_cos[3])
    errors_sin_t_8.append(errors_sin[4])
    errors_cos_t_8.append(errors_cos[4])
    errors_sin_t_9.append(errors_sin[5])
    errors_cos_t_9.append(errors_cos[5])


avg_errors_sin = {'sin_t_4': sum(errors_sin_t_4) / len(errors_sin_t_4), 'sin_t_5': sum(errors_sin_t_5) / len(errors_sin_t_5), 'sin_t_6': sum(errors_sin_t_6) / len(errors_sin_t_6), 'sin_t_7': sum(errors_sin_t_7) / len(errors_sin_t_7), 'sin_t_8': sum(errors_sin_t_8) / len(errors_sin_t_8), 'sin_t_9': sum(errors_sin_t_9) / len(errors_sin_t_9)}
avg_errors_cos = {'cos_t_4': sum(errors_cos_t_4) / len(errors_cos_t_4), 'cos_t_5': sum(errors_cos_t_5) / len(errors_cos_t_5), 'cos_t_6': sum(errors_cos_t_6) / len(errors_cos_t_6), 'cos_t_7': sum(errors_cos_t_7) / len(errors_cos_t_7), 'cos_t_8': sum(errors_cos_t_8) / len(errors_cos_t_8), 'cos_t_9': sum(errors_cos_t_9) / len(errors_cos_t_9)}
sorted_avg_errors_sin = sorted(avg_errors_sin.items(), key=lambda x: x[1])
sorted_avg_errors_cos = sorted(avg_errors_cos.items(), key=lambda x: x[1])

print('Hierarchy of the best approximation for sinus:')
index = 1
for t, error in sorted_avg_errors_sin:
    print(f'{index}. {t} with the minimum error for : {error} times.')
    index += 1

print('Hierarchy of the best approximation for cosinus:')
index = 1
for t, error in sorted_avg_errors_cos:
    print(f'{index}. {t} with the minimum error for : {error} times.')
    index += 1


