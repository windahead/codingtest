param = int(input())

b5 = divmod(param, 5)[0]
isreturn = False
for i in range(b5,-1,-1):
    na = param - (i*5)
    b3 = divmod(na,3)
    if b3[1] == 0 :
        print(i+b3[0])
        isreturn = True
        break

if not isreturn:
    print(-1)
