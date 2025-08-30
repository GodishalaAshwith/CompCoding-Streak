# cook your dish here
N = int(input())
Array = map(int, input().split())
Max_non_zero = 0
non_zero_length = 0
for num in Array:
    if num == 0:
        non_zero_length = 0
    else:
        non_zero_length += 1
    if Max_non_zero < non_zero_length:
        Max_non_zero = non_zero_length
print(Max_non_zero)