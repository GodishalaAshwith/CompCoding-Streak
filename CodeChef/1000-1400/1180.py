# cook your dish here
t = int(input())
for _ in range(t):
    N = int(input())
    Array = sorted(list(map(int, input().split())))
    Array_set = sorted(list(set(Array)))
    Max_count = 0
    Mode = 0
    for num in Array_set:
        if Array.count(num) > Max_count:
            Max_count = Array.count(num)
            Mode = num
    print(Mode, Max_count)