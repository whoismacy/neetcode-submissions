class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for outer_index in range(len(nums)):
        #     remainder = target - nums[outer_index]
        #     for inner_index in range(outer_index + 1, len(nums)):
        #         if remainder == nums[inner_index]:
        #             return [outer_index, inner_index]
        #         else: continue
        dictionary = {}
        for index, _ in enumerate(nums):
            remainder = target - nums[index]
            if remainder in dictionary:
                return [dictionary[remainder], index]
            else:
                dictionary[nums[index]] = index
        return False