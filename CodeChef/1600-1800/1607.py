import math

# cook your dish here
for _ in range(int(input())):
    n, p, k = map(int, input().split())

    # ITERATIVE APPRAOCH - TLE

    # curr=-1
    # ans=0
    # done=False
    # currRem=0
    # while(True):
    #     for i in range(currRem,n,k):
    #         ans+=1
    #         if(i==p):
    #             done=True
    #             break
    #     if(done==True):
    #         break
    #     currRem+=1
    #     if(currRem>=k):
    #         break
    # print(ans)

    # FORMULABASED APPRAOCH, GIVING WRONG ANSWER

    nums_in_one_round = math.ceil(n / k)
    curr_round = (p % k) + 1
    days_in_prev_rounds = (curr_round - 1) * nums_in_one_round
    days_in_curr_round = 0

    # getting the current round, starting from the mod with k increments,
    # untill we get to the desired index
    for i in range(p % k, p + 1, k):
        days_in_curr_round += 1

    leave = (curr_round - 1) - (((n - 1) % k) + 1)
    if ((curr_round - 1) == (((n - 1) % k) + 1) or (((n - 1) % k) + 1) >= curr_round):
        print(days_in_prev_rounds + days_in_curr_round)
    else:
        print(days_in_prev_rounds + days_in_curr_round - leave)