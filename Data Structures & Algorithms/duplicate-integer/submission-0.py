class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        iniSet = set()
        for i in nums:
            iniSet.add(i)
        if (len(nums) == len(iniSet)):
            return False
        else:    
            return True            