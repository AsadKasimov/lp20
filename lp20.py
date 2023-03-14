'Сначала мы определяем функцию `is_multiple_of_n`, которая принимает число и n в качестве входных данных и возвращает `True`, если оно кратно n, в противном случае `False`.'
def is_multiple_of_n(number, n):
    return number % n == 0

'Затем мы определяем функцию `sum_of_multiples_of_n_digit_numbers`, которая принимает n в качестве входных данных и возвращает сумму n-значных чисел, кратных n.'
def sum_of_multiples_of_n_digit_numbers(n):
    total_sum = 0
    'Мы используем два вложенных цикла for для перебора всех возможных комбинаций n-значных чисел и кратных n. Если произведение `num` и `multiple` кратно `n`, мы добавляем его к `total_sum`.'
    for digit in range(1, 10):
        num = digit
        for _ in range(1, n):
            num = num * 10 + digit

        for multiple in range(1, 10):
            if is_multiple_of_n(num * multiple, n):
                total_sum += (num * multiple)

    return total_sum

'Наконец, мы вызываем функцию `sum_of_multiples_of_n_digit_numbers` для n=1-4 и выводим результаты.'
for n in range(1, 5):  # for all n=1,2,3,4
    total_sum = sum_of_multiples_of_n_digit_numbers(n)
    print(f"Сумма кратных {n}-значным числам: {total_sum}")