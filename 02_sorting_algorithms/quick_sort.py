def quick_sort(numbers, left, right, stats):
    if left < right:
        partition_pos = partition(numbers, left, right, stats)

        quick_sort(numbers, left, partition_pos - 1, stats)
        quick_sort(numbers, partition_pos + 1, right, stats)


def partition(numbers, left, right, stats):
    i = left
    j = right - 1
    pivot = numbers[right]

    while i < j:

        while i < right and numbers[i] < pivot:
            stats["comparisons"] += 1
            i += 1

        while j > left and numbers[j] >= pivot:
            stats["comparisons"] += 1
            j -= 1

        if i < j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            stats["swaps"] += 1

    if numbers[i] > pivot:
        stats["comparisons"] += 1
        numbers[i], numbers[right] = numbers[right], numbers[i]
        stats["swaps"] += 1

    return i


numbers = [12, 10, 1, 2, 3, 4, 5, 22]
stats = {"comparisons": 0, "swaps": 0}
quick_sort(numbers, 0, len(numbers) - 1, stats)
print(f"sorted: {numbers}")
print(f"comparisons: {stats["comparisons"]}")
print(f"swaps: {stats["swaps"]}")
