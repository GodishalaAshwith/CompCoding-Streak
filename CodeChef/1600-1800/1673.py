# cook your dish here

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        num = int(input())
        notes = list(map(int, input().split()))

        count = 0;

        maxi = max(notes)

        for i in range(num):
            if notes[i] == 1:
                count += num
                continue

            for j in range(num):

                ele = notes[i] ** (j + 1)

                if (ele > maxi):
                    break;
                if (ele <= notes[j]):
                    count += 1
                j += 1

        print(count)


if __name__ == '__main__':
    main()