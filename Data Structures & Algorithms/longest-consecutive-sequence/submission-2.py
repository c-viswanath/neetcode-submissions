class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 1
        for i in nums:
            if i - 1 not in num_set:
                start = i
                current_length = 1  
                while start + 1 in num_set:
                    current_length += 1
                    start += 1
                longest = max(longest, current_length)
        return longest if nums else 0                    

