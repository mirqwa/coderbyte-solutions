# Have the function palindrome(str) take the str parameter being passed and return the string true if the parameter
# is a palindrome, (the string is the same forward as it is backward) otherwise return the string false.
# The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact
# a palindrome. For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.


def palindrome(strValue):
    str_alpha = "".join(ch for ch in strValue if ch.isalnum())
    str_alpha = str_alpha.lower()
    for i in range(len(str_alpha)):
        if str_alpha[i] != str_alpha[-i - 1]:
            return False
    return True


if __name__ == "__main__":
    print(palindrome("Anne, I vote more cars race Rome-to-Vienna"))
    print(palindrome("Ann, I vote more cars race Rome-to-Vienna"))
