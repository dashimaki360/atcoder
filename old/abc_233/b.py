l, r = map(int, input().split())
s = str(input())
l -= 1

ans = s[:l] + s[l:r][::-1] + s[r:]
print(ans)
