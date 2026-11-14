class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the array first? turn into a set to remove duplicates, then use a for loop?
        # how off from the solution was I? first I hadn't realised the array could have more than one sequence
        # 1st identify all the values that can start a sequence; values that have no left-value (minus one)
        # then count all the subsequent values from the first, return this value

        nums_set = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest