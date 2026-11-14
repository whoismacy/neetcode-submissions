class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem not in vals:
                vals[nums[i]] = i
            else:
                return [vals[rem], i]