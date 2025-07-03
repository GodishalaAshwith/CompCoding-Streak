class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ["a"]
        while len(word)<k:
            nxt = []
            for i in word:
                nxt.append(get_next_char(i))
            word = word + nxt
        return word[k-1]

def get_next_char(char):
    char_code = ord(char)
    next_char_code = char_code + 1
    
    if char.islower() and char == 'z':
        return 'a'
    elif char.isupper() and char == 'Z':
        return 'A'
    
    return chr(next_char_code)