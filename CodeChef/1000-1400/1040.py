# cook your dish here
from collections import Counter

def can_erase_string(S):
    freq = Counter(S)
    for count in freq.values():
        if count % 2 != 0:
            return "NO"
    return "YES"

T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()
    print(can_erase_string(S))