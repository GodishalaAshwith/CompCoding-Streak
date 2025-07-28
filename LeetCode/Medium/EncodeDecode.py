class Solution:
    def encode(self,strs):
        """
        Encodes a list of strings to a single string.
        """
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded
    
    def decode(self,s):
        """
        Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            # Find the separator '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # get the length of the next string
            string = s[j+1:j+1+length]  # extract the string
            res.append(string)
            i = j + 1 + length  # move to the next encoded string
        return res

