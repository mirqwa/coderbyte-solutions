# Have the function look_say_sequence(num) take the num parameter being passed and return the next number in the sequence
# according to the following rule: to generate the next number in a sequence read off the digits of the given number,
# counting the number of digits in groups of the same digit.
# For example, the sequence beginning with 1 would be: 1, 11, 21, 1211, ... The 11 comes from there being "one 1"
# before it and the 21 comes from there being "two 1's" before it. So your program should return the next number
# in the sequence given num.
from collections import defaultdict


def look_say_sequence(num):
    counts = defaultdict(int)
    prev_digit = str(num)[0]
    repeat = 0
    for digit in str(num):
        digit_key = digit
        if digit != prev_digit:
            digit_key = f"{digit}_{repeat}"
            repeat += 1
        possible_keys = [key for key in list(counts.keys()) if key.startswith(digit)]
        if len(possible_keys) > 1:
            digit_key = possible_keys[-1]
        counts[digit_key] += 1
        prev_digit = digit
    results = ""
    for digit, count in counts.items():
        results += f"{count}{digit.split('_')[0]}"
    return results


if __name__ == "__main__":
    print(look_say_sequence(1))
    print(look_say_sequence(11))
    print(look_say_sequence(21))
    print(look_say_sequence(1211))
