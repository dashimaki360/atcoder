x, y = map(str, input().split("."))
if int(y) <= 2:
    print(x + "-")
elif int(y) <= 6:
    print(x)
else:
    print(x + "+")