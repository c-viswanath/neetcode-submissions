class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        minLen = float('inf')

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                minLen = min(minLen, r-l+1)

                curr_sum -= nums[l]
                l += 1
        return minLen if minLen != float('inf') else 0        

