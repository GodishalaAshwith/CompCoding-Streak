# Codeforces submission format

def draw_snake():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    
    for i in range(1, n + 1):
        if i % 2 == 1:  # Odd rows are fully filled with '#'
            sys.stdout.write('#' * m + '\n')
        elif i % 4 == 0:  # Rows like 4th, 8th, etc., have '#' at the beginning
            sys.stdout.write('#' + '.' * (m - 1) + '\n')
        else:  # Rows like 2nd, 6th, etc., have '#' at the end
            sys.stdout.write('.' * (m - 1) + '#\n')

# Call the function directly for Codeforces submission
draw_snake()


# n,m = map(int,input().split())

# res = [['.' for _ in range(m)] for _ in range(n)]

# for i in range(0,n,2):
#     res[i][:] = ["#"]*m

# for i in range(1,n,4):
#     res[i][m-1]="#"

# if n>3:
#     for i in range(3,n,4):
#         res[i][0]="#"

# for i in res:
#     print(*i)