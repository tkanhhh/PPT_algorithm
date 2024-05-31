import numpy as np
import matplotlib.pyplot as plt

def adams_bashforth(f1, f2, t0, u10, u20, h, n):
    t_vals = [t0]
    u1_vals = [u10]
    u2_vals = [u20]

    for _ in range(1, 3):
        t = t_vals[-1]
        u1 = u1_vals[-1]
        u2 = u2_vals[-1]

        k1_u1 = h * f1(t, u1, u2)
        k1_u2 = h * f2(t, u1, u2)
        
        k2_u1 = h * f1(t + h / 2, u1 + k1_u1 / 2, u2 + k1_u2 / 2)
        k2_u2 = h * f2(t + h / 2, u1 + k1_u1 / 2, u2 + k1_u2 / 2)
        
        k3_u1 = h * f1(t + h / 2, u1 + k2_u1 / 2, u2 + k2_u2 / 2)
        k3_u2 = h * f2(t + h / 2, u1 + k2_u1 / 2, u2 + k2_u2 / 2)
        
        k4_u1 = h * f1(t + h, u1 + k3_u1, u2 + k3_u2)
        k4_u2 = h * f2(t + h, u1 + k3_u1, u2 + k3_u2)
        
        u1_next = u1 + (k1_u1 + 2 * k2_u1 + 2 * k3_u1 + k4_u1) / 6
        u2_next = u2 + (k1_u2 + 2 * k2_u2 + 2 * k3_u2 + k4_u2) / 6
        t_next = t + h

        t_vals.append(t_next)
        u1_vals.append(u1_next)
        u2_vals.append(u2_next)

    for _ in range(3, n + 1):
        t = t_vals[-1]
        u1 = u1_vals[-1]
        u2 = u2_vals[-1]

        u1_pred = u1 + (h / 2) * (3 * f1(t, u1, u2) - f1(t - h, u1_vals[-2], u2_vals[-2]))
        u2_pred = u2 + (h / 2) * (3 * f2(t, u1, u2) - f2(t - h, u1_vals[-2], u2_vals[-2]))

        u1_next = u1 + (h / 2) * (f1(t + h, u1_pred, u2_pred) + f1(t, u1, u2))
        u2_next = u2 + (h / 2) * (f2(t + h, u1_pred, u2_pred) + f2(t, u1, u2))
        t_next = t + h

        t_vals.append(t_next)
        u1_vals.append(u1_next)
        u2_vals.append(u2_next)

    return t_vals, u1_vals, u2_vals