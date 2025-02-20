# Have the function dash_insert_2(str) insert dashes ('-') between each two odd numbers and insert asterisks ('*')
# between each two even numbers in str. For example: if str is 4546793 the output should be 454*67-9-3.
# Don't count zero as an odd or even number.


def dash_insert_2(str_num):
    new_str = ""
    for i in range(len(str_num)):
        new_str += str_num[i]
        if i < len(str_num) - 1:
            if int(str_num[i]) % 2 == 0 and int(str_num[i + 1]) % 2 == 0:
                new_str += "*"
            elif int(str_num[i]) % 2 == 1 and int(str_num[i + 1]) % 2 == 1:
                new_str += "-"
    return new_str


if __name__ == "__main__":
    print(dash_insert_2("4546793"))
