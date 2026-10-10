def insertion_sort(numbers):
    n = len(numbers)
    shifts = 0
    comparison = 0

    for i in range(1, n):
        keys = numbers[i]

        j = i - 1
        while j >= 0:
            comparison += 1

            if keys < numbers[j]:
                shifts += 1
                numbers[j + 1] = numbers[j]
                j -= 1
            else:
                break

        numbers[j + 1] = keys

    return numbers, comparison, shifts


my_list = [12, 10, 1, 2, 3, 4, 5, 22]
result = insertion_sort(my_list)
print(f"sorted: {result[0]}")
print(f"comparisons: {result[1]}")
print(f"shifts: {result[2]}")