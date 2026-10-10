def merge_sort(numbers, stats=None):
    if stats is None:
        stats = {"comparisons": 0, "copies": 0}

    if len(numbers) > 1:
        left_arr = numbers[:len(numbers) // 2]
        right_arr = numbers[len(numbers) // 2:]

        merge_sort(left_arr, stats)
        merge_sort(right_arr, stats)

        i = 0  # left_array idx
        j = 0  # right_array idx
        k = 0  # merged_array idx

        while i < len(left_arr) and j < len(right_arr):

            stats["comparisons"] += 1

            if left_arr[i] < right_arr[j]:
                numbers[k] = left_arr[i]
                i += 1
            else:
                numbers[k] = right_arr[j]
                j += 1

            stats["copies"] += 1
            k += 1

        while i < len(left_arr):
            numbers[k] = left_arr[i]
            stats["copies"] += 1
            i += 1
            k += 1

        while j < len(right_arr):
            numbers[k] = right_arr[j]
            stats["copies"] += 1
            j += 1
            k += 1

    return numbers, stats


arr_test = [12, 10, 1, 2, 3, 4, 5, 22]
result, stats = merge_sort(arr_test)
print(f"sorted: {result}")
print(f'comparisons: {stats["comparisons"]}')
print(f"copies: {stats["copies"]}")