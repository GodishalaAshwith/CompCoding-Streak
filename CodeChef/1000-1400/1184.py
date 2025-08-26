for _ in range(int(input())):
    N, P = map(int, input().split())
    problems = list(map(int, input().split()))

    half_of_participants = int(P // 2)
    ten_perc_part = int(P // 10)

    diffic_prob = cakewalk = 0

    for prob in problems:
        if prob <= ten_perc_part:
            diffic_prob += 1
        elif prob >= half_of_participants:
            cakewalk += 1

    print('YES' if diffic_prob == 2 and cakewalk == 1 else 'NO')