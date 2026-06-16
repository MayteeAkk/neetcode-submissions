class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)

        for word in strs:
            word_tup = tuple(sorted(word))
            if word_tup not in word_dict:
                word_dict[word_tup] = [word]
            else:
                word_dict[word_tup].append(word)
        
        return list(word_dict.values())