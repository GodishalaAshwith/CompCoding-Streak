for _ in range(int(input())):
    n = int(input())
    s = input()
    zeros = s.count('0')
    ones = s.count('1')
    print(min(ones, 1 + zeros))