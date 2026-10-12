def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can not divide by zero")
        return None
    except ValueError:
        print("Can not divide by zero")
        return None
    finally:
        print("Program ran successfully")


try:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    print("Result:", divide(num_1, num_2))
except ValueError as e:
    print(f"wrong type of parameters")
finally:
    print("Program ran successfully")

