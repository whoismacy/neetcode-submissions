class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arr, prefix, postfix = [], [i for i in nums], [i for i in nums]
        n, index = len(nums) - 1, 0

        while index <= n:
            if index == 0:
                prefix[index] = nums[index]
            else:
                prefix[index] = nums[index] * prefix[index - 1]
            index = index + 1

        while n >= 0:
            if n == len(nums) - 1:
                postfix[n] = nums[n]
            else:
                postfix[n] = nums[n] * postfix[n + 1]
            n = n - 1

        for i in range(len(nums)):
            if i == 0:
                arr.append(1 * postfix[i+1])
            elif i == len(nums) - 1:
                arr.append(1 * prefix[i-1])
            else:
                arr.append(prefix[i - 1] * postfix[i + 1])

        return arr
