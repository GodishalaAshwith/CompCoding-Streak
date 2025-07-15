def count_distinct_letters(s):
    if s == "{}":
        return 0
    letters_str = s[1:-1].split(", ")
    distinct_letters = set()
    for letter in letters_str:
        distinct_letters.add(letter)
    return len(distinct_letters)

print(count_distinct_letters(input()))