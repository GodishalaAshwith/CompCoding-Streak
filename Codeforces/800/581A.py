def solve(a, b):
    """
    Calculates the number of days Vasya can wear different socks and the number of days he can wear the same socks.
    
    Args:
        a: The number of red socks.
        b: The number of blue socks.
    
    Returns:
        A tuple containing the number of days with different socks and the number of days with the same socks.
    """
    
    days_different = min(a, b)  # Days with different socks
    days_same = (max(a, b) - days_different) // 2  # Days with the same socks
    return days_different, days_same

if __name__ == "__main__":
    a, b = map(int, input().split())
    result = solve(a, b)
    print(*result)