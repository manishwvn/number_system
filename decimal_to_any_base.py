# given a number in decimal base
# to convert into any give base 'b'

def decimal_to_any_base(n, b):
    result = 0
    i = 0

    while(n > 0):

        digit = n % b
        n = n // b

        result += digit * (10 ** i)
        i += 1

    return result


n = int(input())  # given decimal number
b = int(input())  # given base
print(decimal_to_any_base(n, b))
