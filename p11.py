import numpy as np

DATA = np.loadtxt('p11.dat', dtype=int)

products_horizontal = [np.prod(DATA[j][i:i+4]) for i in range(16) for j in range(20)]
products_vertical = [np.prod(DATA.T[j][i:i+4]) for i in range(16) for j in range(20)]
products_diagonal_up = [np.prod([DATA[j+k][i+k] for k in range(4)]) for j in range(16) for i in range(16)]
products_diagonal_down = [np.prod([DATA[j-k][i+k] for k in range(4)]) for i in range(16) for j in range(15, 0, -1)]

print(max(max([products_horizontal, products_vertical, products_diagonal_up, products_diagonal_down])))
