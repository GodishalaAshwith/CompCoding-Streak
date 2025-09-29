import sys
from functools import lru_cache
from io import BytesIO, IOBase
from array import array
from itertools import accumulate, product
import heapq
import bisect
from math import floor, ceil, comb, sqrt,log2, lcm
from collections import defaultdict, deque, Counter
from copy import deepcopy
inf = float('inf')
from functools import lru_cache
from decimal import Decimal
mod = int(1e9) + 7

def solve():
    for _ in range(int(inp())):
        n = int(inp())
        s = inp().strip()
        seen = set()
        if n % 3 == 1:
            print('YES')
        else:
            for first in range(n):
                if first % 3 == 0:
                    seen.add(s[first])
                else:
                    if (n - first - 1) % 3 == 0 and s[first] in seen:
                        print('YES')
                        break
            else:
                print('NO')
if __name__ == "__main__":
    inp, out, flush = sys.stdin.readline, sys.stdout.write, sys.stdout.flush
    solve()