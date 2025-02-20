# Have the function array_addition_i(arr) take the array of numbers stored in arr and return the string true if any
# combination of numbers in the array can be added up to equal the largest number in the array, otherwise return the
# string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because
# 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements,
# and may contain negative numbers


def array_addition_i(arr):
    sorted_arr = sorted(arr)
    max_value = sorted_arr[-1]
    num_sum = 0
    for i in range(len(arr) - 1):
        num_sum += sorted_arr[i]
        for j in range(len(arr) - 1):
            if i != j:
                num_sum += sorted_arr[j]
                if num_sum == max_value:
                    return True
        for k in range(len(arr) - 1):
            if i != k:
                num_sum -= sorted_arr[k]
                if num_sum == max_value:
                    return True
        num_sum = 0
    return False


if __name__ == "__main__":
    print(array_addition_i([4, 6, 23, 10, 1, 3]))
    print(array_addition_i([4, 6, 30, 10, 1, 3]))
