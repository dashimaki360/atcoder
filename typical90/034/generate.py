import random
N = random.randint(4, 10)
K = random.randint(2, N)
print(str(N) + ' ' + str(K))
A = [random.randint(1, 10) for i in range(N)]
print(*A)