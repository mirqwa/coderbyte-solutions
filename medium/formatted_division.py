# Have the function formatted_division(num1,num2) take both parameters being passed, divide num1 by num2, and return
# the result as a string with properly formatted commas and 4 significant digits after the decimal place.
# For example: if num1 is 123456789 and num2 is 10000 the output should be "12,345.6789".
# The output must contain a number in the one's place even if it is a zero.


def formatted_division(num1, num2):
    result = num1 / num2
    return "{:,.4f}".format(result)


if __name__ == "__main__":
    print(formatted_division(123456789, 10000))
    print(formatted_division(123456789, 100000))
