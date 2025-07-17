def count_host_uniform_switch(n, uniforms):
    count = 0
    
    # Loop over all pairs of teams (i, j) where i is the host and j is the guest
    for i in range(n):
        for j in range(n):
            if i != j:
                # If the home uniform color of the host team matches the guest's guest uniform color
                if uniforms[i][0] == uniforms[j][1]:
                    count += 1
    
    return count

# Input
n = int(input())  # number of teams
uniforms = [tuple(map(int, input().split())) for _ in range(n)]  # (home_color, guest_color) pairs

# Output the result
print(count_host_uniform_switch(n, uniforms))
