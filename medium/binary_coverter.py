# Have the function binary_converter(str) return the decimal form of the binary value.
# For example: if 101 is passed return 5, or if 1000 is passed return 8


def binary_converter(num_str):
    dec_value = 0
    for i, value in enumerate(reversed(num_str)):
        dec_value += 2**i * int(value)
    return dec_value


if __name__ == "__main__":
    print(binary_converter("101"))
    print(binary_converter("1000"))
