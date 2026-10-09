number = int(input("Enter the number: "))
step = 0
while number != 1 :
    step += 1
    print(f"step {step}:")
    if number % 2 == 0:
        number /= 2
        print(int(number))
    else :
        number = 3 * number + 1
        print(int(number))
