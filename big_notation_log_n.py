def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        print(f'Low {low} - high {high}')

        mid = (low + high) // 2
        print(f'mid {mid}')
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            print(f'arr[mid] < target ---- {arr[mid]} < {target}')
            low = mid + 1
        else:
            print(f'arr[mid] > target ---- {arr[mid]} > {target}')
            high = mid - 1

    logging.error('Error: target value not found')
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(my_list, 7)
print(result)  # O(log n) - logarithmic time
 
