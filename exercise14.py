import numpy as np
y = [2, 3, 8, 4, 10, 1, 9, 5, 1, 0]
y_übung = (y-np.mean(y))**2
print(y_übung)

y_übung2 = 1/len(y)*np.sum(y_übung)
print(y_übung2)

y_übung3 = y_übung2**(1/2)
print(y_übung3)

