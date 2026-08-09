class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index,num in enumerate(nums):
            numToFind = target - num

            if numToFind in hashMap:
                return [hashMap[numToFind], index]
            hashMap[num] = index     
        return []               
