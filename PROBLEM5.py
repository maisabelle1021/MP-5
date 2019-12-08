import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,199,200)

def a(n):
    b = eval(x)
    return b

x = input('Input equation x(n): ')

for c in range(0,200):
    if c ==0:
        y = (-1.5*a(n)) + (2*a(n+1)) - (0.5*a(n+2))
        
    elif c <= 198:
        y = 0.5*a(n+1) - 0.5*a(n-1)
    
    elif c == 199:
        y = 1.5*a(n) - 2*a(n-1) + 0.5*a(n-2)
        
plt.plot(a(n), color="b", label="x(n)")
plt.plot(y, color ="y", label="y(n)")
plt.grid()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show