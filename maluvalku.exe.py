def main():
    print("Привіт, я калькулятор")
    print("1 - Додавання \
         2 - Віднімання \
             3 - Множення \
             4 - Ділення")
    variant = input("Введіть, що ви хочете зробити:")

    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))

    result = 0
    if variant == '1':
        result = number1 + number2
    elif variant == '2':
        result = number1 - number2
    elif variant == '3':
        result = number1 * number2
    elif variant == '4':
        result = number1 / number2
if __name__ == "__main__":
    main()