class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        preNum = -1
        nums.sort()
        for x in nums:
            if(preNum == x):
                return True
            preNum = x
        return False