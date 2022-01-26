s = str(input())
a, b = map(int, input().split())
a -= 1
b -= 1
ans = list(s)
ans[a] = s[b]
ans[b] = s[a]

print("".join(ans))
