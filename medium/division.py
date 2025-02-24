# Have the function Division(num1,num2) take both parameters being passed and return the Greatest Common Factor.
# That is, return the greatest number that evenly goes into both numbers with no remainder.
# For example: 12 and 16 both are divisible by 1, 2, and 4 so the output should be 4.
# The range for both parameters will be from 1 to 10^3


def division(num1, num2):
    min_number = min(num1, num2)
    max_number = max(num1, num2)
    factor = min_number
    multiple = 1
    while factor > 1:
        if min_number % factor == 0 and max_number % factor == 0:
            return int(factor)
        multiple += 1
        factor = min_number / multiple
    return int(factor)


if __name__ == "__main__":
    print(division(12, 16))
    print(division(120, 160))
    print(division(99, 100))
