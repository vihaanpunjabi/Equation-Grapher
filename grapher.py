import matplotlib.pyplot as plt
import numpy as np
import math

equation = input().lower().replace('^', '**').replace('x', 'x')

x = np.linspace(-50, 50, 100)

def evaluate_equation(equation, x):
    equation = equation.replace('^', '**')
    y = []
    for val in x:
        local_values = {'np': np, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'x': val, 'math': math}
        y.append(eval(equation, local_values))
    return y

y = evaluate_equation(equation, x)
plt.plot(x, y)
plt.title('Graph of ' + equation)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
print('Graphed')

