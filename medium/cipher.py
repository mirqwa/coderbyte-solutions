# Have the function cipher(str,num) take the str parameter and perform a Caesar Cipher shift on it using
# the num parameter as the shifting number. A Caesar Cipher works by shifting each letter in the string N places
# down in the alphabet (in this case N will be num). Punctuation, spaces, and capitalization should remain intact.
# For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".
import string


alphabet = string.ascii_lowercase


def cipher(input, num):
    results = ""
    for char in input:
        if char.lower() not in alphabet:
            results += char
            continue
        char_index = alphabet.index(char.lower())
        new_index = char_index + num
        new_index = new_index % 26 if new_index > 25 else new_index
        new_char = alphabet[new_index]
        new_char = new_char.upper() if char.isupper() else new_char
        results += new_char
    return results


if __name__ == "__main__":
    print(cipher("Caesar Cipher", 2))
    print(cipher("Caesar Cipher Zion", 2))
    print(cipher("Caesar Cipher Zion", 26))
    print(cipher("Caesar Cipher Zion", 54))
