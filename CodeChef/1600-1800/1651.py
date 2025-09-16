for _ in range(int(input())):
    s = input()
    dice = {}
    k = 0
    lens = len(s)
    l = lens - 1
    li = [0] * lens
    flag = 0
    ch = ""
    for i in range(lens):
        if s[i] in dice:
            dice[s[i]].append(i + 1)
        else:
            dice[s[i]] = []
            dice[s[i]].append(i + 1)
    odd = 0
    for i in dice:
        if (len(dice[i]) % 2 != 0):
            odd += 1
    if (odd > 0 and len(s) % 2 == 0):
        flag = 1
    elif (odd != 1 and len(s) % 2 != 0):
        flag = 1
    for i in dice:
        if (len(dice[i]) % 2 == 0):
            for j in range(0, len(dice[i]), 2):
                li[k] = dice[i][j]
                li[l] = dice[i][j + 1]
                k += 1
                l += -1
        else:
            ch = i
    if (lens % 2 != 0):
        for j in range(0, len(dice[ch])):
            li[k] = dice[ch][j]
            k += 1
    if (flag == 1):
        print(-1)
    else:
        print(*li)

