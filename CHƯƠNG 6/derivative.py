# Input data
f_values = {
    -0.3: 1.9507,
    -0.2: 2.0421,
    -0.1: 2.0601
}

h = 0.1

f_prime_forward_0_3 = (f_values[-0.2] - f_values[-0.3]) / h
f_prime_forward_0_2 = (f_values[-0.1] - f_values[-0.2]) / h
f_prime_backward_0_1 = (f_values[-0.1] - f_values[-0.2]) / h

f_double_prime_forward_0_3 = (f_values[-0.1] - 2 * f_values[-0.2] + f_values[-0.3]) / h**2

print(f"f'(-0.3) = {f_prime_forward_0_3}")
print(f"f'(-0.2) = {f_prime_forward_0_2}")
print(f"f'(-0.1) = {f_prime_backward_0_1}")

print(f"f''(-0.3) = {f_double_prime_forward_0_3}")
