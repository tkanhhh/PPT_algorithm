import numpy as np

def euler_method(f, t0, y0, h, n):
    t_vals = [t0]
    y_vals = [y0]

    for _ in range(n):
        t = t_vals[-1]
        y = y_vals[-1]
        
        y_next = y + h * f(t, y)
        t_next = t + h
        
        t_vals.append(t_next)
        y_vals.append(y_next)
    
    return t_vals, y_vals