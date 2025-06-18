def solve():
    a, b = map(int, input().split())
    limak_candies = 0
    bob_candies = 0
    turn = 1
    
    while True:
        if turn % 2 != 0: # Limak's turn
            if limak_candies + turn <= a:
                limak_candies += turn
            else:
                print("Bob")
                return
        else: # Bob's turn
            if bob_candies + turn <= b:
                bob_candies += turn
            else:
                print("Limak")
                return
        turn += 1

t = int(input())
for _ in range(t):
    solve()