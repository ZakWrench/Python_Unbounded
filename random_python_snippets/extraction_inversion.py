def calculare(top, bottom):
    if (top > bottom):
        sum = 0
        for number in range(top - bottom + 1):
            if (number % 2 == 0):
                sum += number
                print(f'current sum: {sum}')
        return print(sum)
    else:
        return 0


# After extraction and inversion:

def is_modulo(number):
    if (number % 2 == 0):
        return number


def calculate(top, bottom):
    if (top < bottom):
        print('top < bottom')
        return
    sum = 0
    for number in range(top - bottom + 1):
        sum += is_modulo(number)
        print(f'current sum: {sum}')
    return print(sum)
