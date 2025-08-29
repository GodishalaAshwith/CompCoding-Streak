# cook your dish here

from collections import Counter

for T in range(int(input())):

    S = Counter(input().strip())

    money = 0
    for v in S.values():
        money += (v + 1) // 2

    print(money)