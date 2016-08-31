primes = [x for x in range(2, 1000) if all(x % y for y in range (2,x))][::-1]

for prime in primes:
    prime = str(prime)
    if prime == prime[::-1]:
        print(prime)
        break