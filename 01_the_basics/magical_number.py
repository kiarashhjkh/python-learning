number = int(input("Enter the number: "))

if number % 3 == 0 and number % 5 == 0:
    print("Legendary Number")
elif number % 3 == 0:
    print("Magical Number")
elif number % 5 == 0:
    print("Cursed Number")
else:
    print("Normal Number")