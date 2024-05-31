def newton_method(f, df, p0, TOL, No):
    i = 1
    while i <= No:
        p = p0 - f(p0) / df(p0)
        if abs(p - p0) < TOL:
            return p
        i += 1
        p0 = p
    return None
