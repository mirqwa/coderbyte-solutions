# Have the function number_search(str) take the str parameter, search for all the numbers in the string,
# add them together, then return that final number divided by the total amount of letters in the string.
# For example: if str is "Hello6 9World 2, Nic8e D7ay!" the output should be 2. First if you add up all the numbers,
# 6 + 9 + 2 + 8 + 7 you get 32. Then there are 17 letters in the string. 32 / 17 = 1.882, and the final answer should
# be rounded to the nearest whole number, so the answer is 2. Only single digit numbers separated by spaces will be
# used throughout the whole string (So this won't ever be the case: hello44444 world).
# Each string will also have at least one letter.


def number_search(strValue):
    num_alpha = 0
    num_sum = 0
    for i in range(len(strValue)):
        if strValue[i].isalpha():
            num_alpha += 1
            continue
        if not strValue[i].isnumeric():
            continue
        if i > 0 and strValue[i - 1].isnumeric():
            continue
        if i < len(strValue) - 1 and strValue[i + 1].isnumeric():
            continue
        num_sum += int(strValue[i])
    return round(num_sum / num_alpha)


if __name__ == "__main__":
    print(number_search("Hello6 9World 2, Nic8e D7ay!"))
