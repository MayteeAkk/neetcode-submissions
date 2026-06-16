class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        word1 = {}
        word2 = {}

        for index in range(len(s)):
            if s[index] not in word1:
                word1[(s[index])] = 1
            else:
                word1[(s[index])] += 1
            if t[index] not in word2:
                word2[(t[index])] = 1
            else:
                word2[t[index]] += 1

        if word1 == word2:
            return True

        return False
        