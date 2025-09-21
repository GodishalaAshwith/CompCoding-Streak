MOD = 10 ** 9 + 7


def count_vowel_matrix_slices(N, K, S):
    # Count the positions of vowels
    vowel_positions = [i for i in range(N) if S[i] in 'aeiou']
    total_vowels = len(vowel_positions)

    # If the number of vowels is not divisible by K, return 0
    if total_vowels % K != 0:
        return 0

    # Number of groups
    groups = total_vowels // K

    # Calculate the number of ways to place dividers
    result = 1
    for i in range(1, groups):
        # Number of positions between the (i*K)th vowel and the (i*K+1)th vowel
        positions = vowel_positions[i * K] - vowel_positions[i * K - 1]
        result = (result * positions) % MOD

    return result


# Read number of test cases
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    S = input().strip()
    result = count_vowel_matrix_slices(N, K, S)
    print(result)