def is_pseudo_sorted(arr):
    n = len(arr)
    bad_index = -1

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if bad_index != -1:
                return False  # More than one inversion
            bad_index = i

    if bad_index == -1:
        return True  # Already sorted

    # Try swapping arr[bad_index] and arr[bad_index + 1]
    arr[bad_index], arr[bad_index + 1] = arr[bad_index + 1], arr[bad_index]

    # Check if sorted after one swap
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Driver code
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print("YES" if is_pseudo_sorted(A) else "NO")
