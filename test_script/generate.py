import random
N = random.randint(4, 10)
K = random.randint(2, N)
print(str(N) + ' ' + str(K))
A = range(1, N+1)
A = list(A)
random.shuffle(A)
print(*A)