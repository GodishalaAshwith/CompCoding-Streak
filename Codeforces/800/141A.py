def amusing_joke():
    # Read input strings
    guest = input().strip()
    host = input().strip()
    pile = input().strip()
    
    # Combine guest and host names
    combined_names = guest + host
    
    # Check if sorted versions match
    if sorted(combined_names) == sorted(pile):
        print("YES")
    else:
        print("NO")

# Call the function for submission on Codeforces
amusing_joke()