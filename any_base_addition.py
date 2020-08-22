# given two numbers of a given base 'b' perform addtion of two numbers and return result

def any_base_addition(n1, n2, b):
    result = 0
    c = 0  # carry
    i = 0
    while(n1 > 0 or n2 > 0 or c > 0):

        d1, d2 = n1 % 10, n2 % 10
        n1, n2 = n1 // 10, n2 // 10

        d = d1 + d2 + c

        c = d // b
        d = d % b

        result += d * (10 ** i)
        i += 1

    return result


n1 = int(input())
n2 = int(input())
b = int(input())  # base of both numbers
print(any_base_addition(n1, n2, b))
