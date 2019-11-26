a, b, c = map(int, input().split())

i = 1
if b >= c:
    print(-1)
    exit(0)
sunsu = c - b
print(divmod(a , sunsu)[0]+1)

