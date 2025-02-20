# Have the function distinct_list(arr) take the array of numbers stored in arr and determine the total number of
# duplicate entries. For example if the input is [1, 2, 2, 2, 3] then your program should output 2 because there are
# two duplicates of one of the elements.


def distinct_list(arr):
    return len(arr) - len(set(arr))


if __name__ == "__main__":
    print(distinct_list([1, 2, 2, 2, 3]))
