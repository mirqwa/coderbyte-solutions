# Have the function multiple_brackets(str) take the str parameter being passed and return 1 #ofBrackets if the brackets
# are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello [world])(!)",
# then the output should be 1 3 because all the brackets are matched and there are 3 pairs of brackets,
# but if str is "((hello [world])" the the output should be 0 because the brackets do not correctly match up.
# Only "(", ")", "[", and "]" will be used as brackets. If str contains no brackets return 1.


def multiple_brackets(strVal):
    brackets_count = 0
    open_brackets = []
    count = 0
    for char in strVal:
        if char in "([":
            count += 1
            open_brackets.append(char)
        elif char in ")]":
            if len(open_brackets) < 1:
                return 0
            open_bracket = open_brackets.pop()
            if char == ")" and open_bracket == "(":
                brackets_count += 1
                count -= 1
            elif char == "]" and open_bracket == "[":
                brackets_count += 1
                count -= 1
            else:
                return 0
    if count == 0 and brackets_count > 0:
        return 1, brackets_count
    elif count == 0:
        return 1
    else:
        return 0



if __name__ == "__main__":
    print(multiple_brackets("(hello [world])(!)"))  # 1 3
    print(multiple_brackets("((hello [world])"))  # 0
    print(multiple_brackets("hello world"))  # 1
    print(multiple_brackets("(hello [world))(!)"))  # 0
