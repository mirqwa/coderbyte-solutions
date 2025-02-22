# Have the function arith_geo(arr) take the array of numbers stored in arr and return the string "Arithmetic"
# if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern.
# If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between
# each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by
# some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].
# Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements


def arith_geo(arr):
    arithmetic = True
    geometric = True
    diff = arr[1] - arr[0]
    factor = arr[1] / arr[0]
    for num, next_num in zip(arr, arr[1:]):
        arithmetic = arithmetic and next_num - num == diff
        geometric = geometric and next_num / num == factor
        if not (arithmetic or geometric):
            return -1
    return "Arithmetic" if arithmetic else "Geometric"


if __name__ == "__main__":
    print(arith_geo([2, 4, 6, 8]))
    print(arith_geo([2, 6, 18, 54]))
    print(arith_geo([2, 6, 18, 51]))
