def binary_search(array, length, target):
    adj_len = length - 1
    result = 0
    while result <= adj_len:
        middle = (adj_len + result) // 2
        if target > array[middle]:
            result = middle + 1
        elif target < array[middle]:
            adj_len = middle - 1
        else:
            return middle, array[middle]

    return print("unsuccessful")


arr = [1, 5, 7, 9, 88, 422, 425, 467, 487, 489, 520, 524, 587, 600]
