def restore_numbers(nums):
    nums.sort()
    total = nums[3]  # this is a + b + c
    a = total - nums[2]
    b = total - nums[1]
    c = total - nums[0]
    return a, b, c

# Example usage:
nums = list(map(int, input().split()))
a, b, c = restore_numbers(nums)
print(a, b, c)
