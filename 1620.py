import sys
read = sys.stdin.readline  # input() 보다 readline이 빠르다!
a, b = map(int, read().split())

pkdict = {}
pklist = []
for i in range(1, a+1):
    param = read().rstrip()
    pkdict[param] = i
    pklist.append(param)

for i in range(b):
    param = read().rstrip()
    if param.isdigit():
        print(pklist[int(param) - 1])
    else:
        print(pkdict[param])
