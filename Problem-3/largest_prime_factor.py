n = 600851475143
temp = n
check_factor = 3
prime_factors = []
while temp > 1:
    if temp%check_factor == 0:
        prime_factors.append(check_factor)
        temp = temp/check_factor
    else:
        check_factor += 2

print(prime_factors[-1])