from math import sqrt

def is_divisible(number):
    for i in range(2, number):
        if i > sqrt(number):
            break
        if not number % i:
            return True
    return False


num_of_primes = 0
primes = []
current_value = 2
while num_of_primes < 1000:
    if not is_divisible(current_value ):
        primes.append(current_value)
        num_of_primes += 1
    current_value += 1
p_sum = 0
for prime in primes:
    p_sum += prime

print(p_sum)
