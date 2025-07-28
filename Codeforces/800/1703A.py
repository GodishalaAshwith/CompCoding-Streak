t = int(input())  # Number of test cases

for _ in range(t):
    s = input().strip()  # Read the string and remove leading/trailing whitespace
    if s.lower() == "yes":
        print("YES")
    else:
        print("NO")
