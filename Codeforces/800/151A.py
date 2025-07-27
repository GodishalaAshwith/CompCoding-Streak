# Input: space-separated values
n, k, l, c, d, p, nl, np = map(int, input().split())

# Calculate total resources
total_drink = k * l
total_slices = c * d
total_salt = p

# Calculate how many toasts we can make from each resource
toasts_from_drink = total_drink // nl
toasts_from_limes = total_slices
toasts_from_salt = total_salt // np

# Minimum of all, divided by number of friends
max_toasts_per_friend = min(toasts_from_drink, toasts_from_limes, toasts_from_salt) // n

# Output the result
print(max_toasts_per_friend)
