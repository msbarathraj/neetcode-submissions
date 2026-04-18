class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        for index, ch in enumerate(strs[0]):
            for word in strs:
                if word[index] != ch:
                    return strs[0][:index]
        
        return strs[0]
