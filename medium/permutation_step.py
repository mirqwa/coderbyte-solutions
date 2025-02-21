# Have the function permutation_step(num) take the num parameter being passed and return the next number greater than
# num using the same digits. For example: if num is 123 return 132, if it's 12453 return 12534.
# If a number has no greater permutations, return -1 (ie. 999).


def permutation_step(num):
    num_str = str(num)
    for i in range(len(num_str) - 1, 0, -1):
        if num_str[i] > num_str[i - 1]:
            right_digits = "".join(sorted(num_str[i - 1] + num_str[i + 1 :]))
            return int(num_str[: i - 1] + num_str[i] + right_digits)
    return -1


if __name__ == "__main__":
    print(permutation_step(123)) # 132
    print(permutation_step(12453)) # 12534
    print(permutation_step(999)) # -1
