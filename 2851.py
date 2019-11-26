inputlist = []
inputlist.append(int(input()))
inputlist.append(int(input()))
inputlist.append(int(input()))
inputlist.append(int(input()))
inputlist.append(int(input()))
inputlist.append(int(input()))
inputlist.append(int(input()))
inputlist.append(int(input()))
inputlist.append(int(input()))
inputlist.append(int(input()))

a =0
idx = 1
for i in inputlist:
    a = a + i
    if a + inputlist[idx] == 100 :
        print(100)
        exit(0)
    elif a + inputlist[idx] > 100 :
        if 100 - a < a+inputlist[idx] - 100 :
            print(a)
            exit(0)
        else :
            print(a+inputlist[idx])
            exit(0)
    if idx < 9 :
        idx = idx + 1

print(a)