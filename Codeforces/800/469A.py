n = int(input())
x_input = list(map(int, input().split()))
y_input = list(map(int, input().split()))

# First number is count, rest are levels
x_levels = set(x_input[1:])
y_levels = set(y_input[1:])

# Union of both players' levels
all_passed = x_levels.union(y_levels)

if len(all_passed) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
