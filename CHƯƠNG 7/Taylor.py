import numpy as np

def taylor_series(f, df_dt, t0, y0, h, n):
    t_vals = [t0]
    y_vals = [y0]

    for _ in range(n):
        t = t_vals[-1]
        y = y_vals[-1]
        
        y_prime = f(t, y)
        y_double_prime = df_dt(t, y)
        
        y_next = y + h * y_prime + (h**2 / 2) * y_double_prime
        t_next = t + h
        
        t_vals.append(t_next)
        y_vals.append(y_next)
    
    return t_vals, y_vals