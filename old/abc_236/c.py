n, m = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

i = 0
for s in S:
    if s == T[i]:
        print("Yes")
        i += 1
    else:
        print("No")
