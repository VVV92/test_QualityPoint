def sum_of_digits(number):
    """
    Функция для вычисления суммы цифр в числе.
    """
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total


def main():
    """
    Главная функция приложения.
    """
    max_number = None
    max_sum = 0

    while True:
        try:
            number = int(input("Введите целое число (0 для выхода): "))
            if number == 0:
                break

            current_sum = sum_of_digits(number)
            if current_sum > max_sum:
                max_sum = current_sum
                max_number = number

        except ValueError:
            print('Неверный формат, введите ЦЕЛОЕ число.')

    if max_number is not None:
        print(f"Число с максимальной суммой цифр: {max_number}")
    else:
        print("Не было введено ни одного числа.")


    input("Нажмите Enter, чтобы выйти...")


if __name__ == "__main__":
    main()