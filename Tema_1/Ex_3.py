import random
import numpy as np
import math

random_numbers = np.random.uniform(-np.pi/2, np.pi/2, 10000)
errors_t_4 = []
errors_t_5 = []
errors_t_6 = []
errors_t_7 = []
errors_t_8 = []
errors_t_9 = []


for number in random_numbers:
    t_4 = (105*number - 10*number**3)/(105 - 45*number**2 + number**4)
    t_5 = (945*number - 105*number**3 + number**5)/(945 - 420*number**2 + 15*number**4)
    t_6 = (10395*number - 1260*number**3 + 21*number**5) / (10395 - 4725*number**2 + 210*number**4 - number**6)
    t_7 = (135135*number - 17325*number**3 + 378*number**5 - number**7) / (135135 - 62370*number**2 + 3150*number**4 - 28*number**6)
    t_8 = (2027025*number - 270270*number**3 + 6930*number**5 - 36*number**7) / (2027025 - 945945*number**2 + 51975*number**4 - 630*number**6 + number**8)
    t_9 = (34459425*number - 4729725*number**3 + 135135*number**5 - 990*number**7 + number**9) / (34459425 - 16216200*number**2 + 945945*number**4 - 13860*number**6 + 45*number**8)
    tangenta = math.tan(number)
    errors = [abs(t_4 - tangenta), abs(t_5 - tangenta), abs(t_6 - tangenta), abs(t_7 - tangenta), abs(t_8 - tangenta), abs(t_9 - tangenta)]
    print('For number:', number, 'the best approximation is:', errors.index(min(errors)) + 4, 'with the error:', min(errors))
    errors_t_4.append(errors[0])
    errors_t_5.append(errors[1])
    errors_t_6.append(errors[2])
    errors_t_7.append(errors[3])
    errors_t_8.append(errors[4])
    errors_t_9.append(errors[5])


avg_erros = {'t_4': sum(errors_t_4)/len(errors_t_4), 't_5': sum(errors_t_5)/len(errors_t_5), 't_6': sum(errors_t_6)/len(errors_t_6), 't_7': sum(errors_t_7)/len(errors_t_7), 't_8': sum(errors_t_8)/len(errors_t_8), 't_9': sum(errors_t_9)/len(errors_t_9)}
sorted_avg_errors = sorted(avg_erros.items(), key=lambda x: x[1])
print('The best approximation is:', sorted_avg_errors[0][0], 'with the average error:', sorted_avg_errors[0][1])
print('The worst approximation is:', sorted_avg_errors[-1][0], 'with the average error:', sorted_avg_errors[-1][1])

print('Hierarchy of the best approximation:')
index = 1
for t, error in sorted_avg_errors:
    print(f'{index}. {t} with the minimum error for : {error} times.')
    index += 1







