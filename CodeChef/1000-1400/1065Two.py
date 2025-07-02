# cook your dish here
for _ in range(int(input())):
    n = int(input())
    gesList = input()
    if "I" in gesList:
        print("INDIAN")
    elif "Y" in gesList:
        print("NOT INDIAN")
    else:
        print("NOT SURE")