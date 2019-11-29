import sys
import math

read = sys.stdin.readline
num = int(read())
until = num + 1

is_primes = [True] * until
max_length = math.ceil(math.sqrt(until))

for i in range(2, max_length):
    if is_primes[i]:
        for j in range(i + i, until, i):
            is_primes[j] = False
primes_list = [i for i in range(2, until) if is_primes[i]]

count = len(primes_list)
s = 0
e = 0
sum = 0
rtn = 0
while True:
    if sum >= num:
        sum -= primes_list[s]
        s += 1
    elif e == len(primes_list):
        break
    else:
        sum += primes_list[e]
        e += 1

    if sum == num:
        rtn += 1

print(rtn)
