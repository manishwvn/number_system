#given two numbers 'n1' and 'n2' of base 'b', given n2 > n1
#subtract n1 from n2 i.e. n2 - n1
def any_base_subtraction(n1, n2, b):
    if n1 > n2:
        n1, n2 = n2, n1

    result = 0
    c = 0 #carry
    i = 1
    #carry is actually the borrow value that takes a -ve value
    while (n2 > 0):
        d1, d2 = n1 % 10, n2 % 10
        n1, n2 = n1 // 10, n2 // 10

        d = 0
        d2 = d2 + c 

        if (d2 >= d1):
            c = 0
            d = d2 - d1
        else:
            c = -1
            d = d2 + b - d1

        result += d * i
        i = i * 10

    return result

n1 = int(input())
n2 = int(input())  # n2 > n1
b = int(input())
print(any_base_subtraction(n1, n2, b))



