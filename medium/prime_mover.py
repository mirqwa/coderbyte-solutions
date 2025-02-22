# Have the function prime_mover(num) return the numth prime number. The range will be from 1 to 10^4.
# For example: if num is 16 the output should be 53 as 53 is the 16th prime number.
import sys


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_mover(num):
    current_number = 0
    for i in range(sys.maxsize):
        if is_prime(i):
            current_number += 1
            if current_number == num:
                return i


if __name__ == "__main__":
    print(prime_mover(16))
