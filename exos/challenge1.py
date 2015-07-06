def generate_primes():
    prime_numbers = []
    index = 2
    count = 0

    def is_prime(n):
        # in the case when n is divisible by a prime number
        # we return False because it is not prime
        for prime_number in prime_numbers:
            if n % prime_number == 0:
                return False

        # after having tested n with every prime number
        # we are sure it is prime
        return True

    while len(prime_numbers) < 1000:
        if is_prime(index):
            prime_numbers.append(index)
            count += 1
        index += 1

    return prime_numbers

print sum(generate_primes())
