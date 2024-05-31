import numpy as np

def midpoint_method(f, t0, y0, h, n):
    t_vals = [t0]
    y_vals = [y0]

    for _ in range(n):
        t = t_vals[-1]
        y = y_vals[-1]
        
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        
        y_next = y + k2
        t_next = t + h
        
        t_vals.append(t_next)
        y_vals.append(y_next)
    
    return t_vals, y_vals

def heun_method(f, t0, y0, h, n):
    t_vals = [t0]
    y_vals = [y0]

    for _ in range(n):
        t = t_vals[-1]
        y = y_vals[-1]
        
        k1 = h * f(t, y)
        k2 = h * f(t + h, y + k1)
        
        y_next = y + 0.5 * (k1 + k2)
        t_next = t + h
        
        t_vals.append(t_next)
        y_vals.append(y_next)
    
    return t_vals, y_vals