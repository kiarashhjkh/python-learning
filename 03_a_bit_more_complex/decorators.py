def decorator(func):
    def wrapper(n):
        import time
        start = time.time()

        result = func(n)

        end = time.time()
        time_taken = end - start

        print(time_taken)
        print(result)

        return result

    return wrapper


@decorator
def n_list_maker(n):
    my_list = []
    for _ in range(1, n + 1):
        my_list.append(_)
    return my_list


n_list_maker(3)
