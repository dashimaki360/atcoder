# 試し割法で素因数をリストで返す
'''
sample
print(prime_factorize(1))
# []

print(prime_factorize(36))
# [2, 2, 3, 3]

print(prime_factorize(840))
# [2, 2, 2, 3, 5, 7]
'''

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a