def skyline(*args):
    max_height = 0
    for arg in args:
        if arg > max_height:
            max_height = arg
    return max_height


my_skill = skyline(1, 1, 1, 1, 1)
print(my_skill)
