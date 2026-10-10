def bubble_sort(numbers):
    comparison = 0
    swaps = 0
    n = len(numbers)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparison += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swaps += 1
                swapped = True
        if swapped == False:
            break
    return numbers, comparison, swaps


my_list = [12, 10, 1, 2, 3, 4, 5, 22]
result = bubble_sort(my_list)
print(f"sorted: {result[0]}")
print(f"comparisons: {result[1]}")
print(f"swaps: {result[2]}")
