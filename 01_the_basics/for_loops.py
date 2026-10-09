
number_of_loops = int(input("Enter the number of events: "))
the_number = int(input("Enter the number: "))

for i in range(number_of_loops):
    if (the_number % 2 == 0):
        the_number /= 2
    else:
        the_number = (2 * the_number) - 1

print(the_number)
