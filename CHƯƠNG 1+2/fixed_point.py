def fixed_point_iteration(g, p0, TOL, No):
    i = 1
    while i <= No:
        p = g(p0)
        if abs(p - p0) < TOL:
            return p
        i += 1
        p0 = p
    return None