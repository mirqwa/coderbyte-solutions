# Have the function number_encoding(str) take the str parameter and encode the message according to the following rule:
# encode every letter into its corresponding numbered position in the alphabet.
# Symbols and spaces will also be used in the input.
# For example: if str is "af5c a#!" then your program should return 1653 1#!.
import string


def number_encoding(strValue):
    alphabet = string.ascii_lowercase
    result = ""
    for char in strValue:
        if char.lower() in alphabet:
            result += str(alphabet.index(char.lower()) + 1)
        else:
            result += char
    return result


if __name__ == "__main__":
    print(number_encoding("af5c a#!"))
