class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count = 0
        # for x in nums:
        #     if(x!=val):
        #         count = count + 1
        # return count
        nums[:] = [x for x in nums if x != val]
        return len(nums)