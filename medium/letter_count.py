# Have the function letter_count(str) take the str parameter being passed and return the first word with the greatest
# number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has
# 2 e's (and 2 t's) and it comes before ever which also has 2 e's.
# If there are no words with repeating letters return -1. Words will be separated by spaces.
import re


def letter_count(str_val):
    words = re.split(r"[^a-zA-Z]", str_val)
    result = None
    max_count = -1
    for word in words:
        for char in set(word):
            current_count = word.lower().count(char.lower())
            if current_count > max_count:
                result = word
                max_count = current_count
    return result


if __name__ == "__main__":
    print(letter_count("Today, is the greatest day ever!"))
