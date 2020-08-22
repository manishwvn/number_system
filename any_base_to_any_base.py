def any_base_to_decimal(n, b):
    result = 0
    i = 0
    while(n > 0):
        digit = n % 10
        n //= 10
        result += digit * (b ** i)
        i += 1

    return result

def decimal_to_any_base(n, b):
    result = 0
    i = 0

    while(n > 0):

        digit = n % b
        n = n // b

        result += digit * (10 ** i)
        i += 1

    return result


def any_base_to_any_base(n, b1, b2):
    n = any_base_to_decimal(n, b1)
    result = decimal_to_any_base(n, b2)

    return result

n = int(input())
b1 = int(input())
b2 = int(input())
print(any_base_to_any_base(n, b1, b2))

