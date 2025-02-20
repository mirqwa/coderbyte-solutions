# Have the function fibonacci_checker(num) return the string yes if the number given is part of the Fibonacci sequence.
# This sequence is defined by: Fn = Fn-1 + Fn-2, which means to find Fn you add the previous two numbers up.
# The first two numbers are 0 and 1, then comes 1, 2, 3, 5 etc. If num is not in the Fibonacci sequence,
# return the string no.


def fibonacci_checker(num):
    fib_1 = 0
    fib_2 = 1
    while fib_2 < num:
        temp = fib_1
        fib_1 = fib_2
        fib_2 = temp + fib_2
    return "yes" if num == fib_2 else "no"


if __name__ == "__main__":
    print(fibonacci_checker(5))
    print(fibonacci_checker(6))
    print(fibonacci_checker(8))
