def has_vowel_and_consonant(word):
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxyz")
    word_lower = word.lower()
    return any(char in vowels for char in word_lower) and any(char in consonants for char in word_lower)


class Solution:
    def isValid(self, word: str) -> bool:
        valid = False
        word = word.lower()
        vowels = set("aeiou")
        consonants = set("bcdfghjklmnpqrstvwxyz")
        if len(word)>=3:
            if word.isalnum():
                if has_vowel_and_consonant(word):
                    valid = True
        return valid