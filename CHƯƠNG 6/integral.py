import numpy as np

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

def simpsons_rule(f, a, b, n):
    h = (b - a) / (n - 1)
    x = np.linspace(a, b, n)
    f_values = f(x)
    return (h/3) * (f_values[0] + 4*sum(f_values[1:-1:2]) + f_values[-1])

def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + (i + 0.5) * h)
    return s * h