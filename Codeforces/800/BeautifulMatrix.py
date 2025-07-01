# Read 5x5 matrix
matrix = [list(map(int, input().split())) for _ in range(5)]

# Find the position of 1
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            # Compute Manhattan distance to center (2,2)
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
            break
