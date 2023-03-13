def is_multiple_of_n(number, n):
    return number % n == 0


def sum_of_multiples_of_n_digit_numbers(n):
    total_sum = 0

    for digit in range(1, 10):
        num = digit
        for _ in range(1, n):
            num = num * 10 + digit

        for multiple in range(1, 10):
            if is_multiple_of_n(num * multiple, n):
                total_sum += (num * multiple)

    return total_sum


for n in range(1, 5):  # for all n=1,2,3,4
    total_sum = sum_of_multiples_of_n_digit_numbers(n)
    print(f"Сумма кратных {n}-значным числам: {total_sum}")