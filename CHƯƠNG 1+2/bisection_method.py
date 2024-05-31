def bisection_method(f, a, b, TOL, No):
    i = 1
    FA = f(a)
    
    while i <= No:
        p = a + (b - a) / 2 
        print(a, p, b)
        FP = f(p)
        if FP == 0 or (b - a) / 2 < TOL:
            return p 
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    
    return None