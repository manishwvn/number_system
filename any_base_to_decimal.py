#given a number 'n' of base 'b'
#convert the number to decimal

def any_base_to_decimal(n, b):
    result = 0
    i = 0
    while(n > 0):
        digit = n % 10
        n //= 10
        result += digit * (b ** i)
        i += 1

    return result

n = int(input())
b = int(input())
print(any_base_to_decimal(n, b))
