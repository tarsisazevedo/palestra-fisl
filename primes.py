import math

def fill_sieve(number):
    return [index for index in xrange(2, number + 1)]

def remove_zeros(sieve):
    return [sieve[index] for index in xrange(len(sieve)) if sieve[index]]

def sieve_of_erastostenes(number):
    sieve = fill_sieve(number)
    limit = int(math.sqrt(number))

    for index1 in xrange(0, limit):
        if not sieve[index1]:
            continue

        for index2 in xrange(index1 + 1, number - 1):
            if sieve[index2] and (not (sieve[index2] % sieve[index1])):
                sieve[index2] = 0

    return sieve

def primes_to(number):
    sieve = sieve_of_erastostenes(number)
    return remove_zeros(sieve)
