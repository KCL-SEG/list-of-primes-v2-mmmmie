"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    list.append(2)
    candidate = list[-1] + 1
    while len(list) < number_of_primes:
        is_prime = True
        for number in list:
            if candidate % number == 0:
                is_prime = False
        if is_prime:
            list.append(candidate)
        candidate += 1
    return list
