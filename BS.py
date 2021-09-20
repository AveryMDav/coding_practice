def binary_search(array, arr_len, target):
    rec_len = 0
    len_down_1 = arr_len - 1
    while rec_len <= len_down_1:
        middle = (rec_len + len_down_1) // 2
        if target > array[middle]:
            rec_len = middle + 1
        elif target < array[middle]:
            len_down_1 = middle - 1
        else:
            return array[middle]

    return print("unsuccessful")


arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 48, 100, 151, 202, 543, 666, 1001, 2025, 2121]

print(binary_search(arr, len(arr), 3000))


