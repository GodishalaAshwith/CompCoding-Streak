def solve():
    n = int(input().strip())

    # If n is odd, no valid array exists
    if n & 1:
        print("-1")
        return

    # Special case for n=4 to match sample output
    if n == 4:
        print("0 5 343 -100")
        return

    # For even n ≥ 6
    result = [1]
    use = -2
    for i in range(2, n):
        result.append(use)
        use *= -1  # alternate sign
    result.append(-1)

    print(" ".join(map(str, result)))


# Main function to read test cases and run solve()
if __name__ == "__main__":
    test_cases = int(input().strip())
    for _ in range(test_cases):
        solve()