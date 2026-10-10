def selection_sort(numbers):
    n = len(numbers)
    swaps = 0
    comparison = 0

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparison += 1
            if numbers[j] < numbers[min_index]:
                min_index = j

        if min_index != i:
            swaps += 1
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers, comparison, swaps


my_list = [12, 10, 1, 2, 3, 4, 5, 22]
result = selection_sort(my_list)
print(f"sorted: {result[0]}")
print(f"comparisons: {result[1]}")
print(f"swaps: {result[2]}")
