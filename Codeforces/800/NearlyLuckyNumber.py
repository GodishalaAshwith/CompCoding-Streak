n = input()  # Read the number as a string

# Count how many lucky digits are in n
lucky_count = sum(1 for digit in n if digit in '47')

# Check if lucky_count is itself a lucky number
if all(d in '47' for d in str(lucky_count)):
    print("YES")
else:
    print("NO")
