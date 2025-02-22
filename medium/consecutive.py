# Have the function consecutive(arr) take the array of integers stored in arr and return the minimum number of
# integers needed to make the contents of arr consecutive from the lowest number to the highest number.
# For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the
# array (5 and 7) to make it a consecutive array of numbers from 4 to 8.
# Negative numbers may be entered as parameters and no array will have less than 2 elements.


def consecutive(arr):
    arr = sorted(arr)
    diff = arr[-1] - arr[0]
    return diff - len(arr) + 1


if __name__ == "__main__":
    print(consecutive([4, 8, 6]))
    print(consecutive([-1, 10]))
