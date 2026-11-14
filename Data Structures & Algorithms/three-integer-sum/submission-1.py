class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # how do we tackle this with two pointers?
        # we use two pointers on both ends and then for each
        # addition we loop within the bounds of l and r to look for an equivalent
        # after watching the solution I wasn't badly off all I needed was to
        # start with the initial value then the two pointers and sort the array
        
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = val + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res