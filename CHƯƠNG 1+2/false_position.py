def false_position_method(f, p0, p1, TOL, No):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    
    if q0 * q1 > 0:
        print("Sử dụng phương pháp khác")
        return None
    
    while i <= No:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) < TOL:
            return p
        i += 1
        q = f(p)
        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    
    return None