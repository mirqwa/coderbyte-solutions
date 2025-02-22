# Have the function prime_checker(num) take num and return 1 if any arrangement of num comes out to be a prime number,
# otherwise return 0. For example: if num is 910, the output should be 1 because 910 can be
# arranged into 109 or 019, both of which are primes.
import itertools


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_checker(num):
    num_str = str(num)
    for val in itertools.permutations(num_str, len(num_str)):
        if is_prime(int("".join(val))):
            return 1
    return 0


if __name__ == "__main__":
    print(prime_checker(910))
    print(prime_checker(900))
