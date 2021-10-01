s = 0
try:
    n = int(input('Введите число: '))
except ValueError:
    print('Введите целое число')
else:
    if n < 0:
        n *= -1
    if n == 0:
        print('Сумма всех цифр числа равна 0')
    while n > 0:
        a = n % 10
        n //= 10
        if a % 2 == 1:
            s += a
    print('Сумма всех цифр числа -', s)

