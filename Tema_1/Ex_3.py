import random
import numpy as np
import math

random_numbers = np.random.uniform(-np.pi/2, np.pi/2, 10000)
print(random_numbers)
errors_t_4 = []
errors_t_5 = []
errors_t_6 = []
errors_t_7 = []
errors_t_8 = []
errors_t_9 = []

for number in random_numbers:
    t_4 = (105*number - 10*number**3)/(105 - 45*number**2 + number**4)
    t_5 = (945*number - 105*number**3 + number**5)/(945 - 420*number**2 + 15*number**4)
    t_6 = (10395 - 1260*number**3 + 21*number**5) / (10395 - 4725*number**2 + 210*number**4 - number**6)
    t_7 = (135135*number - 17325*number**3 + 378*number**5 - number**7) / (135135 - 62370*number**2 + 3150*number**4 - 28*number**6)
    t_8 = (2027025*number - 270270*number**3 + 6930*number**5 - 36*number**7) / (2027025 - 945945*number**2 + 51975*number**4 - 630*number**6 + number**8)
    t_9 = (34459425*number - 4729725*number**3 + 135135*number**5 - 990*number**7 + number**9) / (34459425 - 16216200*number**2 + 945945*number**4 - 13860*number**6 + 45*number**8)
    tangenta = math.tan(number)
    
